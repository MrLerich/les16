from models import *
from config import db
import json


#
# def insert_data_user(input_data: list):
#     """Вставляет данные в User построчно"""
#     for row in input_data:
#         db.session.add(
#             User(
#                 id=row.get("id"),
#                 first_name=row.get("first_name"),
#                 last_name=row.get("last_name"),
#                 age=row.get("age"),
#                 email=row.get("email"),
#                 role=row.get("role"),
#                 phone=row.get("phone")
#             )
#         )
#
#     db.session.commit()
#
#
# def insert_data_order(input_data: list):
#     """Вставляет данные в Order построчно"""
#     for row in input_data:
#         db.session.add(
#             Order(
#                 id=row.get("id"),
#                 name=row.get("name"),
#                 description=row.get("description"),
#                 start_date=row.get("start_date"),
#                 end_date=row.get("end_date"),
#                 address=row.get("address"),
#                 price=row.get("price"),
#                 customer_id=row.get("customer_id"),
#                 executor_id=row.get("executor_id")
#             )
#         )
#
#     db.session.commit()
#
#
# def insert_data_offer(input_data: list):
#     """Вставляет данные в Offer построчно"""
#     for row in input_data:
#         db.session.add(
#             Offer(
#                 id=row.get("id"),
#                 order_id=row.get("order_id"),
#                 executor_id=row.get("executor_id")
#             )
#         )
#
#     db.session.commit()


def insert_data_universal(model, input_data: list):  # на вход подается модель и входные данные:list
    """Вставляет данные в (model: User, Order, Offer) построчно. Универсальный вариант."""
    for row in input_data:  # итерируемся по каждой строчке
        db.session.add(model(**row))  # добавляем данные с распаковкой (ключ-значение)
    db.session.commit()


def init_db():
    """При старте приложения положит наши данные в таблицы"""
    db.drop_all()
    db.create_all()
    with open("data/user.json") as file:
        data = json.load(file)
        insert_data_universal(User, data)

    with open("data/order.json") as file:
        data = json.load(file)
        insert_data_universal(Order, data)

    with open("data/offer.json") as file:
        data = json.load(file)
        insert_data_universal(Offer, data)


def get_all(model) -> dict:
    """Возвращает все данные из нужных таблиц в форме словаря(model: User, Order, Offer)"""
    result = []
    for row in db.session.query(model).all():  # итерируемся по всем записям
        result.append(row.to_dict())  # уже есть ф-я приведения к словарю to_dict

    return result


def get_all_by_id(model, user_id):
    """Возвращает данные по id (model: User, Order, Offer)"""
    try:
        return db.session.query(model).get(user_id).to_dict()
    except Exception as e:
        print(e)
        return f"Данных по идентификатору {user_id}  в таблице {model} не найдено"


def update_universal(model, user_id, values: dict):
    """Обновляет данные в таблице,при условии, что все ключи указаны в values точно есть в базе,
    могут быть пустыми"""
    try:
        db.session.query(model).filter(model.id == user_id).update(values)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Что-то пошло не так"


def delete_universal(model, user_id):
    """Удаляет данные из таблицы (model: User, Order, Offer)"""
    try:
        db.session.query(model).filter(model.id == user_id).delete()
        db.session.commit()
    except Exception as e:
        print(e)
        return "Что-то пошло не так, данные не удалены"

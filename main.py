import json
from flask import request
from config import app
from models import User, Order, Offer
from utils import get_all, insert_data_universal, get_all_by_id, update_universal, delete_universal, init_db


@app.route("/users/", methods=['GET', 'POST'])
def get_users():

    if request.method == 'GET':  # определяем какой метод у нас
        data = get_all(User)  # нужная модель данных
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        # какаие данные у нас приходят(нужно list)
        if isinstance(request.json, list):
            insert_data_universal(User, request.json)  # универсальным методом кладем данные в нужную модель
        elif isinstance(request.json, dict):
            insert_data_universal(User, [request.json])
        else:
            print("Непонятный тип данных")

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/orders/", methods=['GET', 'POST'])
def get_orders():

    if request.method == 'GET':  # определяем какой метод у нас
        data = get_all(Order)  # нужная модель данных
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        # какаие данные у нас приходят(нужно list)
        if isinstance(request.json, list):
            insert_data_universal(Order, request.json)  # универсальным методом кладем данные в нужную модель
        elif isinstance(request.json, dict):
            insert_data_universal(Order, [request.json])
        else:
            print("Непонятный тип данных")

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers/", methods=['GET', 'POST'])
def get_offers():

    if request.method == 'GET':  # определяем какой метод у нас
        data = get_all(Offer)  # нужная модель данных
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        # какие данные у нас приходят(нужно list)
        if isinstance(request.json, list):
            insert_data_universal(Offer, request.json)  # универсальным методом кладем данные в нужную модель
        elif isinstance(request.json, dict):
            insert_data_universal(Offer, [request.json])  # dict оборачиваем в list
        else:
            print("Непонятный тип данных")

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/users/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_user_by_id(user_id):
    if request.method == 'GET':
        data = get_all_by_id(User, user_id)
        return app.response_class(
            response=json.dumps(data, indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "PUT":
        update_universal(User, user_id, request.json)
        #универсальным методом обновления выбираем модель по PK где обновляем и значения обновления
        return app.response_class(
            response=json.dumps(["Данные изменены успешно!"], indent=4, ensure_ascii=False),
            status=20,
            mimetype='application/json'
        )
    elif request.method == 'DELETE':
        delete_universal(User, user_id)
        #универсальным удалением выбираем модельи что удаляем по PK
        return app.response_class(
            response=json.dumps(["Удалено успешно!"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )

@app.route("/orders/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_order_by_id(user_id):
    if request.method == 'GET':
        data = get_all_by_id(Order, user_id)
        return app.response_class(
            response=json.dumps(data, indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "PUT":
        update_universal(Order, user_id, request.json)
        return app.response_class(
            response=json.dumps(["Данные изменены успешно!"], indent=4, ensure_ascii=False),
            status=20,
            mimetype='application/json'
        )
    elif request.method == 'DELETE':
        delete_universal(Order, user_id)
        return app.response_class(
            response=json.dumps(["Удалено успешно!"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )

@app.route("/offers/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_offer_by_id(user_id):
    if request.method == 'GET':
        data = get_all_by_id(Offer, user_id)
        return app.response_class(
            response=json.dumps(data, indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "PUT":
        update_universal(Offer, user_id, request.json)
        return app.response_class(
            response=json.dumps(["Данные изменены успешно!"], indent=4, ensure_ascii=False),
            status=20,
            mimetype='application/json'
        )
    elif request.method == 'DELETE':
        delete_universal(Offer, user_id)
        return app.response_class(
            response=json.dumps(["Удалено успешно!"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
if __name__ == '__main__':
    init_db()
    app.run(host='127.0.0.1', port=8080, debug=True)

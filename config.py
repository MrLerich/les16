from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
# Путь/URI базы данных, который будет использоваться для подключения
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Если установлен в True, то Flask-SQLAlchemy будет отслеживать изменения объектов
# и посылать сигналы. По умолчанию  None, что включает отслеживание но выводит
# предупреждение, что в будующем будет отключена по умолчанию.
# Данная функция требует дополнительную память, и должна быть отключена если не используется.

db = SQLAlchemy(app)  # связываем нашу бд с app

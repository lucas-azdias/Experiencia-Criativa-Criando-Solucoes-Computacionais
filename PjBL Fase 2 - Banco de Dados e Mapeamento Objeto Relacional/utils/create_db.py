from flask import Flask

from models import *


def create_db(app: Flask):
    # Criação do banco de dados
    with app.app_context():
        db.drop_all()
        db.create_all()

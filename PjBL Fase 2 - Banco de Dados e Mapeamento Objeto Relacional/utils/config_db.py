from flask import Flask

from sqlalchemy import text

from models import *


def config_db(app:Flask):
    # Configuração inicial do banco de dados
    with app.app_context():
        with open("models/insert_database.sql", "r", encoding="UTF-8") as file:
            lines = file.readlines()
            query = ""
            for line in lines:
                if not line.startswith("--") and not line.startswith("#") and line.strip("\n"):
                    query += line.strip("\n")
                    if query.endswith(";"):
                        db.session.execute(text(query))
                        db.session.commit()
                        query = ""

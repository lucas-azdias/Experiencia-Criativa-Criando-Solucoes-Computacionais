from flask import Flask, render_template

from controllers.admin_controller import admin
from controllers.auth_controller import auth
from controllers.plants_controller import plants
from controllers.payment_controller import payment
from controllers.sensors_controller import sensors

from models import db, instance, login_manager


def createApp() -> Flask:
    # Criando o FlaskApp
    app = Flask(__name__, template_folder="../views/", static_folder="../static/")

    # Registrando Blueprints
    app.register_blueprint(admin, url_prefix="/admin")
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(plants, url_prefix="/plants")
    app.register_blueprint(payment, url_prefix="/payment")
    app.register_blueprint(sensors, url_prefix="/sensors")
    
    # Configurações do FlaskApp
    app.config["TESTING"] = False
    app.config["SECRET_KEY"] = "segredo"
    app.config["SQLALCHEMY_DATABASE_URI"] = instance

    # Configurações do DataBase
    db.init_app(app)

    # Configurações do Gerenciador de Login
    login_manager.init_app(app)

    @app.route('/')
    def index():
        return render_template("index.html")

    return app

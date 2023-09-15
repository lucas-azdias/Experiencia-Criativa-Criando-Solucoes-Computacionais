from flask import Flask, render_template

from controllers.auth_controller import auth
from controllers.plants_controller import plants
from controllers.payment_controller import payment
from controllers.sensors_controller import sensors


def createApp() -> Flask:
    app = Flask(__name__, template_folder="../views/", static_folder="../static/")

    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(plants, url_prefix="/plants")
    app.register_blueprint(payment, url_prefix="/payment")
    app.register_blueprint(sensors, url_prefix="/sensors")
    
    app.config["SECRET_KEY"] = "segredo"

    @app.route('/')
    def index():
        return render_template("index.html")

    return app

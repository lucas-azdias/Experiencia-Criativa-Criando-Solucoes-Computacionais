from flask import Flask, render_template

from controllers.admin_controller import admin
from controllers.auth_controller import auth
from controllers.plants_controller import plants
from controllers.payment_controller import payment
from controllers.sensors_controller import sensors

from models import db, instance, login_manager, mqtt_client, topics_subscribed


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
    app.config['MQTT_BROKER_URL'] = 'broker.hivemq.com'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = ''
    app.config['MQTT_PASSWORD'] = ''
    app.config['MQTT_KEEPALIVE'] = 5
    app.config['MQTT_TLS_ENABLED'] = False

    # Configurações do MQTT Client
    mqtt_client.init_app(app)

    # Configurações do DataBase
    db.init_app(app)

    # Configurações do Gerenciador de Login
    login_manager.init_app(app)

    @app.route('/')
    def index():
        return render_template("index.html")
    
    # Handler da conexão do MQTT
    @mqtt_client.on_connect()
    def mqtt_connection_handler(client, userdata, flags, rc):
        if rc == 0:
            print("MQTT conectado com sucesso")
            for topic in topics_subscribed:
                mqtt_client.subscribe(topic)
        else:
            print("MQTT não foi conectado")
    
    # Handler das mensagens recebidas do MQTT
    @mqtt_client.on_message()
    def mqtt_message_handler(client, userdata, message):
        from models import Record
        from json import loads
        try:
            data = loads(message.payload.decode())
            with app.app_context():
                Record.insert_record(id_sensor=int(data['id_sensor']), value=float(data['value']))
        except:
            print("Mensagem inválida detectada")

    return app

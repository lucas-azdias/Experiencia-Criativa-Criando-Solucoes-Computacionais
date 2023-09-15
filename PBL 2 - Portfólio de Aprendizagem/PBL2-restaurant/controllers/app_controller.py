from flask import Flask, render_template, session, g
from controllers.admin_controller import admin
from controllers.auth_controller import auth

from models import db, instance, login_manager

def create_app() -> Flask:
    app = Flask(__name__, template_folder="./views/", 
                        static_folder="./static/", 
                        root_path="./")
    
    app.config["TESTING"] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config["SQLALCHEMY_DATABASE_URI"] = instance
    db.init_app(app)

    login_manager.init_app(app)

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(admin, url_prefix='/admin')
    

    @app.route('/')
    def index():
        return render_template("home.html")
    
    return app
from flask import Flask, render_template, session, g
from controllers.base_controller import base
from controllers.auth_controller import auth
from controllers.billing_controller import billing
from controllers.payment_controller import payment
from controllers.people_controller import people
from controllers.product_controller import product
from controllers.ticket_controller import ticket
from controllers.iot_controller import iot

app = Flask(__name__, template_folder="./views/", static_folder="./static/")

app.register_blueprint(base, url_prefix='/base')

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(billing, url_prefix='/billing')
app.register_blueprint(payment, url_prefix='/payment')
app.register_blueprint(people, url_prefix='/people')
app.register_blueprint(product, url_prefix='/product')
app.register_blueprint(ticket, url_prefix='/ticket')
app.register_blueprint(iot, url_prefix='/iot')


@app.route('/')
def index():
    return render_template("home.html")



if __name__ == "__main__":
    app.run(debug=True)
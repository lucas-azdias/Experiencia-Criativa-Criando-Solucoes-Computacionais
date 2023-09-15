from flask import Blueprint, render_template,redirect,url_for

payment = Blueprint("payment", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@payment.route("/")
def payment_index():
    return render_template("/payment/payment_index.html")
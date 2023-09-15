from flask import Blueprint, render_template,redirect,url_for

billing = Blueprint("billing", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@billing.route("/")
def billing_index():
    return render_template("/billing/billing_index.html")
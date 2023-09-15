from flask import Blueprint, render_template, redirect,url_for
from flask_login import current_user, login_required
from controllers.billing_controller import billing
from controllers.payment_controller import payment
from controllers.people_controller import people
from controllers.product_controller import product
from controllers.ticket_controller import ticket
from controllers.iot_controller import iot

admin = Blueprint("admin", __name__, 
                    template_folder="./views/", 
                    static_folder='./static/', 
                    root_path="./")

admin.register_blueprint(billing, url_prefix='/billing')
admin.register_blueprint(payment, url_prefix='/payment')
admin.register_blueprint(people, url_prefix='/people')
admin.register_blueprint(product, url_prefix='/product')
admin.register_blueprint(ticket, url_prefix='/ticket')
admin.register_blueprint(iot, url_prefix='/iot')

@admin.route("/")
@admin.route("/admin")
@login_required
def admin_index():
    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))
    else:
        return render_template("admin/admin_base.html", name = current_user.username)

    
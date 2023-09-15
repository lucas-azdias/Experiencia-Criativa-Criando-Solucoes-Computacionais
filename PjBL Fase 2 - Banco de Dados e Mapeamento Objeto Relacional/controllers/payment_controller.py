from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from models import User, Payment

from datetime import datetime


payment = Blueprint("payment", __name__, template_folder="./views/", static_folder="./static/", root_path="./")

MONTH_SIGNING_VALUE = 19.99


def add_payment(username, date) -> bool:
    value = MONTH_SIGNING_VALUE

    date = date.split("-")
    try:
        date_year = int(date[0])
        date_month = int(date[1])
    except:
        date_month = None
        date_year = None

    # Verifica se há alguma informação vazia
    info = [date_month, date_year]
    if None in info or "" in info:
        # Informações inválidas
        flash("Informações inválidas", "danger")
        return False

    # Se haver um usuário com esse username, adiciona o pagamento
    user = User.get_user_by_username(username)
    if user:
        Payment.insert_payment(user.id_user, value, *info, True, user.card_num_card,
                               user.card_name_owner, user.card_cvv, user.card_month_expire_date, 
                               user.card_year_expire_date)
        
        # Pagamento efetuado com sucesso
        flash("Pagamento efetuado com sucesso", "success")
        return True
    else:
        # Erro no pagamento
        flash("Erro no pagamento", "warning")
        return False


@payment.route("/")
@login_required
def payment_index():
    payments = User.get_user(current_user.id_user).payments
    payments_info = [
        [
            payment.value,
            f"{payment.year}/{str(payment.month):0>2}",
            "Pago" if payment.is_paid else "Em aberto",
            payment.date_payment
        ] for payment in payments
    ]
    return render_template("/payment/payment_index.html", payments_info=payments_info)


@payment.route("/register_payment")
@login_required
def payment_register_payment():
    current_month_year = datetime.today().strftime("%Y-%m")
    month_signing_value = str(MONTH_SIGNING_VALUE)
    return render_template("/payment/payment_register_payment.html", current_month_year=current_month_year, month_signing_value=month_signing_value)


@payment.route("/add_payment", methods=["POST"])
@login_required
def payment_add_payment():
    username = current_user.username
    date = datetime.today().strftime("%Y-%m")

    add_payment(username, date)
    
    return redirect(url_for("payment.payment_index"))

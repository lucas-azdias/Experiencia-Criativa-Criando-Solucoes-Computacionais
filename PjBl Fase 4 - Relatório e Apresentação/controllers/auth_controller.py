from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user

from models import User

from datetime import datetime


auth = Blueprint("auth", __name__, template_folder="./views/", static_folder="./static/", root_path="./")


def add_user(username, name, email, phone, password, confirm_password, is_admin, card_num_card, card_name_owner, card_cvv, card_expire_date) -> bool:
    if not current_user.is_authenticated:
        is_admin = False

    card_expire_date = card_expire_date.split("-")
    try:
        card_month_expire_date = int(card_expire_date[0])
        card_year_expire_date = int(card_expire_date[1])
    except:
        card_month_expire_date = None
        card_year_expire_date = None

    # Verifica se há alguma informação vazia
    info = [username, name, email, phone, password, is_admin, card_num_card,
            card_name_owner, card_cvv, card_month_expire_date, card_year_expire_date]
    if None in info or "" in info:
        # Informações inválidas
        flash("Informações inválidas", "danger")
        return False

    # Pega todos os usernames
    usernames = [user.username for user in User.get_users()]

    # Se não haver repetição de username e senha for confirmada, adiciona usuário
    hasUsername = username in usernames
    isPasswordConfirmed = password == confirm_password
    if not hasUsername and isPasswordConfirmed:
        user = User.insert_user(*info)

        # Registrado com sucesso
        flash("Registrado com sucesso", "success")

        if not current_user.is_authenticated:
            login_user(user)

        return True
    else:
        if not isPasswordConfirmed:
            # Senha não confirmada
            flash("Senha de acesso não confirmada", "warning")
        elif hasUsername:
            # Usuário já cadastrado
            flash("Usuário já cadastrado", "warning")

        return False


@auth.route("/")
def auth_index():
    if not current_user.is_authenticated:
        return render_template("/auth/auth_index.html")
    else:
        # Já autenticado
        flash("Já autenticado", "warning")
        return redirect(url_for("index"))


@auth.route("/login", methods=["POST"])
def auth_login():
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.get_user_by_username(username)

    if not user or not user.verify_password(password):
        # Nome de usuário e/ou senha incorretos
        flash("Nome de usuário e/ou senha incorretos", "danger")
        return redirect(url_for("auth.auth_index"))
    
    login_user(user)

    # Logado com sucesso
    flash("Logado com sucesso", "success")
    if user.is_admin:
        return redirect(url_for("admin.admin_users_manager"))
    else:
        return redirect(url_for("index"))


@auth.route("/logout")
@login_required
def auth_logout():
    logout_user()
    # Deslogado com sucesso
    flash("Deslogado com sucesso", "success")
    return redirect(url_for("auth.auth_index"))
    

@auth.route("/register_user")
def auth_register_user():
    if not current_user.is_authenticated:
        current_month_year = datetime.today().strftime("%Y-%m")
        return render_template("/auth/auth_register_user.html", current_month_year=current_month_year)
    else:
        # Já autenticado
        flash("Já autenticado", "warning")
        return redirect(url_for("index"))


@auth.route("/add_user", methods=["POST"])
def auth_add_user():
    # Dados do usuário
    username = request.form.get("username")
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")

    # Cartão de crédito
    card_num_card = request.form.get("card_num_card")
    card_name_owner = request.form.get("card_name_owner")
    card_cvv = request.form.get("card_cvv")
    card_expire_date = request.form.get("card_expire_date")

    # Permissão padrão
    is_admin = False

    add_user(username, name, email, phone, password, confirm_password,
             is_admin, card_num_card, card_name_owner, card_cvv, card_expire_date)

    return redirect(request.referrer)

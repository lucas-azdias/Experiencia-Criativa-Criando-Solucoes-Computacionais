from flask import Blueprint, request, render_template, redirect, url_for


auth = Blueprint("auth", __name__, template_folder="./views/", static_folder="./static/", root_path="./")


# DADOS PUXADOS DO BANCO DE DADOS
users = [("admin", "12345678", True), ("roberto", "gomes", False), ("bafome", "jesus", True)] # (username, password, is_admin)

isLogged = False
isAdmin = False


@auth.route("/")
def auth_index():
    global isLogged, isAdmin
    if not isLogged:
        isAdmin = False
        return render_template("/auth/auth_index.html")
    else:
        return redirect(url_for("index"))


@auth.route("/login", methods=["POST"])
def auth_login():
    username = request.form.get("username")
    password = request.form.get("password")

    ifAdmin = (username, password, True) in users
    ifComum = (username, password, False) in users

    global isLogged, isAdmin
    if ifAdmin or ifComum:
        isLogged = True
        if ifAdmin:
            isAdmin = True
            return redirect(url_for("auth.auth_users_manager"))
        else:
            isAdmin = False
            return redirect(url_for("index"))
    else:
        isLogged = False
        isAdmin = False
        return redirect(url_for("auth.auth_index"))
    

@auth.route("/register_user")
def auth_register_user():
    return render_template("/auth/auth_register_user.html")


@auth.route("/users_manager")
def auth_users_manager():
    if isLogged and isAdmin:
        usernames = [user[0] for user in users]
        is_admin = [user[2] for user in users]
        return render_template("/auth/auth_users_manager.html", usernames=usernames, is_admin=is_admin)
    elif isLogged and not isAdmin:
        return redirect(url_for("index"))
    else:
        return redirect(url_for("auth.auth_index"))


@auth.route("/add_user", methods=["POST"])
def auth_add_user():
    username = request.form.get("username")
    password = request.form.get("password")

    if isLogged and isAdmin:
        is_admin = request.form.get("is_admin")
        if is_admin == None:
            return redirect(url_for("auth.auth_users_manager"))
        is_admin = int(is_admin)
    else:
        is_admin = 0

    usernames = [user[0] for user in users]

    user = (username, password, True if is_admin == 1 else False)
    if not username in usernames:
        users.append(user)
    else:
        # Flash -> Erro - usuário já cadastrado
        if isLogged and isAdmin:
            return redirect(url_for("auth.auth_users_manager"))
        else:
            return redirect(url_for("auth.auth_register_user"))
    
    if isLogged and isAdmin:
        return redirect(url_for("auth.auth_users_manager"))
    else:
        return redirect(url_for("index"))

from flask import Blueprint, request, render_template, redirect, url_for


payment = Blueprint("payment", __name__, template_folder="./views/", static_folder="./static/", root_path="./")


# DADOS PUXADOS DO BANCO DE DADOS
usernames = ["admin", "roberto", "bafome"]
last_index = 2
cards = {"bafome": [(0, "Bafomé", "1956786311112222", "2024-01", "123")], "roberto": [(1, "Roberto Gomes", "1956786311110000", "2024-03", "000"), (2, "Gomes Roberto", "1956786300002222", "2025-08", "999")]}  # "username": ((name_card, id_card, exp_date, cvv), ...)

isLogged = True
isAdmin = True
loggedUsername = "bafome"


@payment.route("/")
def payment_index():
    return render_template("/payment/payment_index.html", cards=cards)


@payment.route("/register_card")
def payment_register_card():
    return render_template("/payment/payment_register_card.html")


@payment.route("/payment_manager")
def payment_payment_manager():
    if isLogged and isAdmin:
        return render_template("/payment/payment_payment_manager.html", cards=cards, usernames=usernames)
    elif isLogged and not isAdmin:
        return redirect(url_for("index"))
    else:
        return redirect(url_for("auth.auth_index"))


@payment.route("/add_card", methods=["POST"])
def payment_add_card():
    username = request.form.get("username")
    name_card = request.form.get("name_card")
    id_card = request.form.get("id_card")
    exp_date = request.form.get("exp_date")
    cvv = request.form.get("cvv")

    global last_index
    if isLogged and not isAdmin and not username == loggedUsername:
        return redirect(url_for("index"))
    elif not isLogged and not isAdmin:
        return redirect(url_for("auth.auth_index"))
    
    if username != "" and name_card != "" and id_card != "" and exp_date != "" and cvv != "":
        if not username in cards.keys():
            cards[username] = list()
        last_index += 1
        cards[username].append((last_index, name_card, id_card, exp_date, cvv))
    return redirect(url_for("payment.payment_payment_manager"))


@payment.route("/del_card", methods=["POST"])
def payment_del_card():
    id_card = int(request.form.get("id_card_del"))

    if isLogged and isAdmin:
        for k, v in cards.items():
            for i in range(len(v)):
                if v[i][0] == id_card:
                    cards[k].pop(i)

    if isLogged and isAdmin:
        return url_for("payment.payment_payment_manager")
    else:
        return url_for("index")

from flask import Blueprint, render_template,redirect,url_for

ticket = Blueprint("ticket", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@ticket.route("/")
def ticket_index():
    return render_template("/ticket/ticket_index.html")
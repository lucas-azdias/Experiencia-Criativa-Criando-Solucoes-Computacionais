from flask import Blueprint, render_template, redirect, url_for

auth = Blueprint("auth", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

@auth.route("/")
def auth_index():
    return render_template("auth/auth_index.html")
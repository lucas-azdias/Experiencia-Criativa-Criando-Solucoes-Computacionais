from flask import Blueprint, render_template,redirect,url_for

people = Blueprint("people", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@people.route("/")
def people_index():
    return render_template("/people/people_index.html")
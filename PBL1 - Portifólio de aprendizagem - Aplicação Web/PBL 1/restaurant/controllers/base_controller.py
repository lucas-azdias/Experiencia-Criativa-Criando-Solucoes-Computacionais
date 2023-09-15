from flask import Blueprint, render_template, redirect, url_for

base = Blueprint("base", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

@base.route("/")
def base_index():
    return render_template("base/base_index.html")


@base.route('/form_example')
def base_form_example():
    return render_template("base/view_example.html")
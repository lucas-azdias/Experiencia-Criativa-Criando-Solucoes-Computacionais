from flask import Blueprint, render_template,redirect,url_for

product = Blueprint("product", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@product.route("/")
def products_index():
    return render_template("/product/product_index.html")
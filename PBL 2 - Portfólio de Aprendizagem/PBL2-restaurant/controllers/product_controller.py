from flask import Blueprint, render_template, redirect, url_for, flash, request
from models import Product, Ingredient, ProductIngredients

product = Blueprint("product", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@product.route("/")
def products_index():
    return redirect(url_for("admin.admin_index"))


@product.route("/products")
def products_products():
    return render_template("/product/product_index.html")


@product.route("/register_product")
def products_register_product():
    return render_template("/product/register_product.html")


@product.route("/save_product", methods=["POST"])
def products_save_product():
    name = request.form.get("name")
    current_price = request.form.get("current_price")
    available_quantity = request.form.get("available_quantity")
    description = request.form.get("description")
    info = [name, current_price, available_quantity, description]
    if not None in info and not "" in info:
        try:
            current_price = float(current_price)
            available_quantity = int(available_quantity)
        except:
            flash("Erro")
            return redirect(request.referrer)
        Product.insert_product(*info)
        flash("Sucesso")
        return redirect(url_for("admin.product.products_view_products"))
    else:
        flash("Erro")
        return redirect(request.referrer)


@product.route("/view_products")
def products_view_products():
    products = Product.query.all()
    return render_template("/product/view_products.html", products=products)


@product.route("/ingredients")
def products_ingredients():
    return render_template("/product/ingredient_index.html")


@product.route("/register_ingredient")
def products_register_ingredient():
    return render_template("/product/register_ingredient.html")


@product.route("/save_ingredient", methods=["POST"])
def products_save_ingredient():
    name = request.form.get("name")
    available_quantity = request.form.get("available_quantity")
    info = [name, available_quantity]
    if not None in info and not "" in info:
        try:
            available_quantity = int(available_quantity)
        except:
            flash("Erro")
            return redirect(request.referrer)
        Ingredient.insert_ingredient(*info)
        flash("Sucesso")
        return redirect(url_for("admin.product.products_view_ingredients"))
    else:
        flash("Erro")
        return redirect(request.referrer)


@product.route("/view_ingredients")
def products_view_ingredients():
    ingredients = Ingredient.query.all()
    return render_template("/product/view_ingredients.html", ingredients=ingredients)


@product.route("/connect_product_ingredients")
def products_connect_product_ingredients():
    products = Product.query.all()
    ingredients = Ingredient.query.all()
    return render_template("/product/connect_product_ingredients.html", products=products, ingredients=ingredients)


@product.route("/save_product_ingredients", methods=["POST"])
def products_save_product_ingredients():
    id_product = request.form.get("id_product")
    id_ingredient = request.form.get("id_ingredient")
    info = [id_product, id_ingredient]
    if not None in info and not "" in info:
        ProductIngredients.insert_product_ingredients(*info)
        flash("Sucesso")
        return redirect(url_for("admin.product.products_view_products"))
    else:
        flash("Erro")
        return redirect(request.referrer)

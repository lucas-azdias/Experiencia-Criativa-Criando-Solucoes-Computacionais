from flask import Blueprint, request, render_template, redirect, url_for


plants = Blueprint("plants", __name__, template_folder="./views/", static_folder="./static/", root_path="./")


saved_plants = []


@plants.route('/')
def plants_index():
    global saved_plants
    return render_template('plants/plants_index.html', saved_plants=saved_plants)


@plants.route('/register_plant')
def plants_register_plant():
    global saved_plants
    return render_template('plants/plants_register_plant.html', saved_plants=saved_plants)


@plants.route('/save_plant', methods=['POST'])
def plants_save_plant():
    nome_planta = request.form.get("nome_planta")
    sensor = request.form.get("sensor")
    umidade = request.form.get("umidade")
    global saved_plants 
    saved_plants.append("Planta " + nome_planta + ", Sensor " + sensor + ", Umidade mínima " + umidade)
    return redirect(url_for("plants.plants_index"))

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from models import Sensor, Record


sensors = Blueprint("sensors", __name__, template_folder="./views/", static_folder="./static/", root_path="./")


@sensors.route('/')
def sensors_index():
    sensors = current_user.sensors
    return render_template("sensors/sensors_index.html", sensors=sensors)


@sensors.route('/show_records')
@login_required
def sensors_show_records():
    sensors = current_user.sensors

    id_sensor = request.args.get("id_sensor_selected")

    if not id_sensor:
        records = None
    else:
        try:
            records = []
            for record in Sensor.get_sensor(int(id_sensor)).records:
                records.append(record)
        except:
            records = None
            
    return render_template("sensors/sensors_show_records.html", sensors=sensors, records=records)


@sensors.route('/register_sensor')
@login_required
def sensors_register_sensor():


    return render_template("sensors/sensors_register_sensor.html")

@sensors.route('/select_sensor', methods=['POST' ,'GET'])
@login_required
def sensors_select_sensor():

    id_sensor = request.form.get("id_sensor")

    print(f'--------------------------{id_sensor}')
    if id_sensor:
        return redirect(url_for("sensors.sensors_update_sensor") + "?id_sensor_selected=" + str(id_sensor))
    else:
        return render_template("sensors/sensors_select_sensor.html")


@sensors.route('/update_sensor' , methods = ['POST'  ,'GET'])
@login_required
def sensors_update_sensor():

    id_sensor = request.args.get("id_sensor_selected")
    sensor = Sensor.get_sensor(id_sensor)

    
    id_s = request.form.get("id_sensor")
    name = request.form.get("name")
    model = request.form.get("model")
    brand = request.form.get("brand")
    measure = request.form.get("measure")
    voltage = request.form.get("voltage")

    info = [name, model, brand, measure, voltage]

    if not None in info:
        Sensor.update_sensor(id_sensor = id_s,name=name,model = model,brand = brand,measure = measure,voltage=voltage)
        flash("Atualizado com sucesso", "sucess")
        return redirect(url_for("sensors.sensors_index"))
    else:
        if sensor:
            return render_template("sensors/sensors_update_sensor.html" , sensor = sensor)  
        else:
            flash("Sensor nao encontrado", "danger")
            return render_template("sensors/sensors_select_sensor.html")

@sensors.route('/add_sensor', methods=['POST'])
@login_required
def sensors_add_sensor():

    name = request.form.get("name")
    model = request.form.get("model")
    brand = request.form.get("brand")
    measure = request.form.get("measure")
    voltage = request.form.get("voltage")

    info = [name, model, brand, measure, voltage]

    if not None in info:
        sensor = Sensor.insert_sensor(current_user.id_user, *info)
        flash("Cadastrado com sucesso", "success")
        return redirect(url_for("sensors.sensors_show_records") + "?id_sensor_selected=" + str(sensor.id_sensor))
    else:
        flash("Erro no cadastro", "danger")
        return redirect(url_for("sensors.sensors_add_sensor"))


@sensors.route('/add_record', methods=['POST'])
@login_required
def sensors_add_record():
    id_sensor = request.form.get("id_sensor")
    value = request.form.get("value")

    info = [id_sensor, value]

    if not None in info:
        Record.insert_record(*info, None)
        flash("Cadastrado com sucesso", "success")
        return redirect(url_for("sensors.sensors_show_records") + "?id_sensor_selected=" + str(id_sensor))
    else:
        flash("Erro no cadastro", "danger")
        return redirect(url_for("sensors.sensors_show_records"))


@sensors.route('/update_record', methods=['POST'])
@login_required
def sensors_update_record():

    id_record = request.form.get("id_record")
    value = request.form.get("value")

    info = [id_record, value]
    
    if not None in info:
        Record.update_record(id_record = id_record , value = value)
        flash("Cadastrado com sucesso", "success")
        return redirect(url_for("sensors.sensors_show_records"))
    else:
        flash("Erro no cadastro", "danger")
        return redirect(url_for("sensors.sensors_show_records"))
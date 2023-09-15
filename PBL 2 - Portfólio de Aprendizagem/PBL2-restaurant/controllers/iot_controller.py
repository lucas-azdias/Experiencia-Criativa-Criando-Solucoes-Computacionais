from flask import Blueprint, render_template,redirect,url_for, request, flash
from models import Sensor, Device, db
iot = Blueprint("iot", __name__, template_folder = './views/admin/', static_folder='./static/', root_path="./")

@iot.route("/")
def iot_index():
    return render_template("/iot/iot_index.html")

@iot.route("/register_sensor")
def register_sensor():
    return render_template("/iot/register_sensor.html")

@iot.route("/view_sensors")
def view_sensors():
    sensors = Sensor.get_sensors()
    return render_template("/iot/view_sensors.html", sensors = sensors)

@iot.route("/save_sensors", methods = ["POST"])
def save_sensors():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    description = request.form.get("description")
    measure = request.form.get("measure")
    voltage = request.form.get("voltage")
    is_active = True if request.form.get("is_active") == "on" else False

    Sensor.save_sensor(name, brand, model, description ,voltage, is_active, measure)

    return redirect(url_for('admin.iot.view_sensors'))

@iot.route("/update_sensor/<id>")
def update_sensor(id):
    sensor = db.session.query(Device, Sensor)\
                        .join(Sensor, Sensor.id == Device.id)\
                        .filter(Sensor.id == int(id)).first()
    
    return render_template("/iot/update_sensor.html", sensor = sensor)

@iot.route("/save_sensor_changes", methods = ["POST"])
def save_sensor_changes():
    data = request.form.copy()
    data["is_active"] = data.get("is_active") == "on"
    Sensor.update_sensor(data)
    return redirect(url_for("admin.iot.view_sensors"))

@iot.route("/delete_sensor/<id>")
def delete_sensor(id):
    if Sensor.delete_sensor(id):
        flash("Dispositivo Sensor Excluído com sucesso!!", "success")
    else:
        flash("Dispositivo Sensor não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.iot.view_sensors"))


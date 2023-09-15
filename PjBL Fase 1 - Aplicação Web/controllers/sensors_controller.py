from flask import Blueprint, render_template



sensors = Blueprint("sensors", __name__, template_folder="./views/", static_folder="./static/", root_path="./")


@sensors.route('/')
def sensors_index():
    return render_template('sensors/sensors_index.html')

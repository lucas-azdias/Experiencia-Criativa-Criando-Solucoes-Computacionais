from models import db, User

from datetime import datetime


class Sensor(db.Model):
    __tablename__ = "sensors"
    id_sensor = db.Column(db.Integer(), primary_key=True)
    id_user = db.Column(db.Integer(), db.ForeignKey(User.id_user))
    name = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False, default="")
    brand = db.Column(db.String(50), nullable=False, default="")
    measure = db.Column(db.String(20), nullable=False, default="")
    voltage = db.Column(db.Float(), nullable=False)
    register_date = db.Column(db.DateTime(), nullable=False, default=datetime.now())

    # Relações 1:N
    records = db.relationship("Record", backref="sensors", lazy=True)
    plants = db.relationship("Plant", backref="sensors", lazy=True)


    def insert_sensor(id_user, name, model, brand, measure, voltage, register_date=None):
        if not register_date:
            register_date = datetime.now()
        sensor = Sensor(id_user=id_user, name=name, model=model,
                        brand=brand, measure=measure, voltage=voltage)
        db.session.add(sensor)
        db.session.commit()
        return sensor
    


    def update_sensor(id_sensor, id_user=None, name=None, model=None, brand=None, measure=None, voltage=None):

        sensor = Sensor.get_sensor(id_sensor)

        if id_user:
            sensor.id_user = id_user
        if name:
            sensor.name = name
        if model:
            sensor.model = model
        if brand:
            sensor.brand = brand
        if measure:
            sensor.measure = measure
        if voltage:
            sensor.voltage = voltage
        
        db.session.commit()
        return sensor


    def get_sensor(id_sensor):
        sensor = Sensor.query.filter_by(id_sensor=id_sensor).first()
        return sensor


    def get_sensors():
        sensors = Sensor.query.all()
        return sensors
    

    def delete_sensor(id_sensor):
        sensor = Sensor.get_sensor(id_sensor)
        sensor.delete()
        db.session.commit()


    def get_by_name(name):
        sensor = Sensor.query.filter_by(name=name).first()
        return sensor
from models import db, Device

class Actuator(db.Model):
    __tablename__ = "actuators"
    id = db.Column("actuator_id", db.Integer(), db.ForeignKey(Device.id), primary_key=True)
    actuator_type = db.Column(db.String(30))

    #activations = ....
from models import db, Device

class Microcontroller(db.Model):
    __tablename__ = "microcontrollers"
    id = db.Column("id", db.Integer(), db.ForeignKey(Device.id), primary_key=True)
    ports = db.Column(db.Integer())

    alerts = db.relationship("Alert", backref="microcontrollers", lazy=True)
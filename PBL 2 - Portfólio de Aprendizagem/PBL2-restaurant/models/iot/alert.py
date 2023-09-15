from models import db, Microcontroller
from datetime import datetime

class Alert(db.Model):
    __tablename__ = "alerts"
    id = db.Column("id", db.Integer(), primary_key=True)
    microcontroller_id = db.Column("microcontroller_id", db.Integer(), db.ForeignKey(Microcontroller.id))
    message = db.Column(db.String(100), nullable=False, default="Alerta!!")
    date_time = db.Column("date_time", db.DateTime(), nullable=False, default=datetime.now())
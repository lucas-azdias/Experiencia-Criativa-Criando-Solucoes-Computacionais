from models.db import db
from models import Waiter 
from models import Payment

class WorkingTimeRecord(db.Model):
    __tablename__ = 'working_time_records'
    id = db.Column(db.Integer(), primary_key=True)
    waiter_id = db.Column(db.Integer(), db.ForeignKey(Waiter.id), nullable=False)
    payment_id = db.Column(db.Integer(), db.ForeignKey(Payment.id), nullable=True)
    record_datetime = db.Column(db.DateTime, nullable = False)
    number_of_hours = db.Column(db.Float, nullable = False)
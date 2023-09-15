from models.db import db
from models import Employee

class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer(), primary_key=True)
    employee_id = db.Column(db.Integer(), db.ForeignKey(Employee.id))
    payment_datetime = db.Column(db.DateTime(), nullable=False)
    reference_date = db.Column(db.Date(), nullable=True)
    payment_value = db.Column(db.Float(), nullable=True)

    working_time_records = db.relationship('WorkingTimeRecord', backref='payments')
    orders = db.relationship('Order', backref='payments')
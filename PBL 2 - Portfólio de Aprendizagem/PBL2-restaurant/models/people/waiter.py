from models.db import db
from models import Employee 

class Waiter(db.Model):
    __tablename__ = "waiters"
    id = db.Column(db.Integer, db.ForeignKey(Employee.id), primary_key=True)
    hour_price = db.Column(db.Float)

    orders = db.relationship('Order', backref='waiters')
    working_time_records = db.relationship('WorkingTimeRecord', backref='waiters')
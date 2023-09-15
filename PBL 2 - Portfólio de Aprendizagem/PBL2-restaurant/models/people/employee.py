from models.db import db
from models import Person, User

class Employee(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer(), db.ForeignKey(Person.id), primary_key=True) # primary keys are required by SQLAlchemy
    user_id = db.Column(db.Integer(), db.ForeignKey(User.id))
    created_at = db.Column(db.Date())

    payments = db.relationship('Payment', backref='employees')
    general_services = db.relationship('GeneralService', backref='employees')
    waiters = db.relationship('Waiter', backref='employees')

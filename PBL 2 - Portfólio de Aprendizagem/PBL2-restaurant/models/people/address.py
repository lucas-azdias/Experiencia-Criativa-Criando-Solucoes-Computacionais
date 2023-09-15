from models.db import db
from models import Person

class Address(db.Model):
    __tablename__ = "addresses"
    id = db.Column(db.Integer(), primary_key=True) # primary keys are required by SQLAlchemy
    person_id = db.Column(db.Integer(), db.ForeignKey(Person.id))
    address = db.Column(db.String(200))
    state = db.Column(db.String(2))
    city = db.Column(db.String(100))
    district = db.Column(db.String(100))
    number = db.Column(db.String(100))
    complement = db.Column(db.String(100))
    zip_code = db.Column(db.String(15))
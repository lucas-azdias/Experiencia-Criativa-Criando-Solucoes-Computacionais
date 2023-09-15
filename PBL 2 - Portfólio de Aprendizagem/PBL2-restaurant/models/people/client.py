from models.db import db
from models import Person

class Client(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer(), db.ForeignKey(Person.id), primary_key = True)
    created_at = db.Column(db.Date())

    tickets =  db.relationship('Ticket', backref='clients')

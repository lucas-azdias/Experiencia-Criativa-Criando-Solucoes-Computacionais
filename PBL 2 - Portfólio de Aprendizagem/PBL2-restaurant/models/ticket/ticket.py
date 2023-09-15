from models.db import db
from models import Client
from models import Billing

class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer(), primary_key=True)
    client_id = db.Column(db.Integer(), db.ForeignKey(Client.id, ondelete='CASCADE'))
    billing_id = db.Column(db.Integer(), db.ForeignKey(Billing.id), nullable=True)
    creation_datetime = db.Column(db.DateTime, nullable = False)
    purchase_total = db.Column(db.Float, nullable=True)
    items = db.Column(db.Integer, nullable = False, default = '0')

    orders = db.relationship('Order', backref='tickets')

    def save_tickets():
        pass

    def get_tickets():
        pass
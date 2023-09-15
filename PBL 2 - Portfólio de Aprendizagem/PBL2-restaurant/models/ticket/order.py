from models.db import db
from models import Ticket
from models import Waiter 
from models import Payment
from models import Product

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer(), primary_key=True)
    ticket_id = db.Column(db.Integer(), db.ForeignKey(Ticket.id, ondelete='CASCADE'), nullable=False)
    product_id = db.Column(db.Integer(), db.ForeignKey(Product.id), nullable=False)
    waiter_id = db.Column(db.Integer(), db.ForeignKey(Waiter.id), nullable=False)
    payment_id = db.Column(db.Integer(), db.ForeignKey(Payment.id), nullable=True)
    creation_datetime = db.Column(db.DateTime, nullable = False)
    product_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable = False, default = '1')

    def save_orders():
        pass

    def get_orders():
        pass
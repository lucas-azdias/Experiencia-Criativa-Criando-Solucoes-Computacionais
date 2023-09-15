from models.db import db

class Billing(db.Model):
    __tablename__ = 'billings'
    id = db.Column('id', db.Integer(), primary_key=True)
    value = db.Column(db.Float())
    billing_date = db.Column(db.DateTime())

    billing_forms = db.relationship('BillingForm', back_populates = "billings", secondary='billing_billing_forms')
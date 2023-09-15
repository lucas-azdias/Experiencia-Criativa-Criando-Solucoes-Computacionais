from models.db import db

class BillingForm(db.Model):
    __tablename__ = "billing_forms"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))

    billings = db.relationship('Billing', back_populates = "billing_forms", secondary='billing_billing_forms')
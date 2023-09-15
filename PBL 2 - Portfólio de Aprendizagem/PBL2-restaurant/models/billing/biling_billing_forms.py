from models.db import db
from models import Billing
from models import BillingForm

class BillingBillingForms(db.Model):
    __tablename__ = 'billing_billing_forms'
    id = db.Column(db.Integer(), primary_key=True)
    billing_id = db.Column(db.Integer(), db.ForeignKey(Billing.id, ondelete='CASCADE'))
    billing_form_id = db.Column(db.Integer(), db.ForeignKey(BillingForm.id, ondelete='CASCADE'))
    value = db.Column(db.Float())
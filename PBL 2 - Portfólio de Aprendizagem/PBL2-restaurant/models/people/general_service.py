from models.db import db
from models import Employee 

class GeneralService(db.Model):
    __tablename__ = "general_services"
    id = db.Column(db.Integer(), db.ForeignKey(Employee.id), primary_key=True) # primary keys are required by SQLAlchemy
    salary = db.Column(db.Float())
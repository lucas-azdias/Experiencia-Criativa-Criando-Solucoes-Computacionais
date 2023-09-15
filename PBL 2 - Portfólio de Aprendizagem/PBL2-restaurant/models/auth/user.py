from werkzeug.security import check_password_hash
from models import db, login_manager

class User(db.Model):
    __tablename__ = "users"
    id = db.Column("id",  db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(1024), nullable=False) 

    roles = db.relationship("Role", back_populates="users", secondary="user_roles")
    reads = db.relationship("Read", backref="users", lazy=True)    

    # Métodos necessários para o Flask-Login
    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False
    
    # User-loader do Flask-Login
    @login_manager.user_loader
    def get_user(id):
        return User.query.filter_by(id=id).first()


    def get_id(self):
        return str(self.id)
    
    def verify_password(self, password):
        return check_password_hash(self.password, password)

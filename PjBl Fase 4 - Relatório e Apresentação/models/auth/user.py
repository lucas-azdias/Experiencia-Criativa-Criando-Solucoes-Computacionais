from models import db, login_manager

from datetime import datetime


class User(db.Model):
    __tablename__ = "users"
    id_user = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(14), nullable=False)
    password = db.Column(db.String(512), nullable=False)
    is_admin = db.Column(db.Boolean(), nullable=False, default=False)
    date_creation = db.Column(db.Date(), nullable=False, default=datetime.today())

    # Cartão de crédito
    card_num_card = db.Column(db.String(16), nullable=False)
    card_name_owner = db.Column(db.String(50), nullable=False)
    card_cvv = db.Column(db.String(3), nullable=False)
    card_month_expire_date = db.Column(db.Integer(), nullable=False)
    card_year_expire_date = db.Column(db.Integer(), nullable=False)

    # Relações 1:N
    payments = db.relationship("Payment", backref="users", lazy=True)
    sensors = db.relationship("Sensor", backref="users", lazy=True)

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
    def get_user(id_user):
        return User.query.filter_by(id_user=id_user).first()


    def get_id(self):
        return str(self.id_user)
    

    def verify_password(self, password):
        return self.password == password
    

    def insert_user(username, name, email, phone, password, is_admin, card_num_card, card_name_owner, card_cvv, card_month_expire_date, card_year_expire_date, date_creation=None):
        if not date_creation:
            date_creation = datetime.today()
        user = User(username=username, name=name, email=email,
                    phone=phone, password=password, is_admin=is_admin,
                    card_num_card=card_num_card, card_name_owner=card_name_owner,
                    card_cvv=card_cvv, card_month_expire_date=card_month_expire_date,
                    card_year_expire_date=card_year_expire_date)
        db.session.add(user)
        db.session.commit()
        return user
    

    def update_user(id_user, username=None, name=None, email=None, phone=None, password=None, is_admin=None, card_num_card=None, card_name_owner=None, card_cvv=None, card_month_expire_date=None, card_year_expire_date=None):
        user = User.get_user(id_user)
        if username:
            user.username = username
        if name:
            user.name = name
        if email:
            user.email = email
        if phone:
            user.phone = phone
        if password:
            user.password = password
        if is_admin:
            user.is_admin = is_admin
        if card_num_card:
            user.card_num_card = card_num_card
        if card_name_owner:
            user.card_name_owner = card_name_owner
        if card_cvv:
            user.card_cvv = card_cvv
        if card_month_expire_date:
            user.card_month_expire_date = card_month_expire_date
        if card_year_expire_date:
            user.card_year_expire_date = card_year_expire_date
        db.session.commit()
        return user


    def get_users():
        users = User.query.all()
        return users
    
    
    def get_user_by_username(username):
        user = User.query.filter_by(username=username).first()
        return user
    

    def delete_user(id_user):
        user = User.get_user(id_user)
        user.delete()
        db.session.commit()

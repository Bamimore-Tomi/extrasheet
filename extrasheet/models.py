from . import db

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, index=True)
    phone_number = db.Column(db.String(15))
    gender = db.Column(db.String(100))
    date_of_birth = db.Column(db.Date())
    password_hash = db.Column(db.String(128))
    
    def __str__(self):
        return self.email
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self , password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(str(self.password_hash), password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
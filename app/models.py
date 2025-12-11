from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default='user')  # user, manager, admin
    
    def __repr__(self):
        return f'<User {self.username}>'

class Ensemble(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))  # оркестр, группа, квартет и т.д.
    description = db.Column(db.Text)
    image_url = db.Column(db.String(200))
    
    def __repr__(self):
        return f'<Ensemble {self.name}>'

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    catalog_number = db.Column(db.String(50), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(100))
    release_date = db.Column(db.Date)
    retail_price = db.Column(db.Float)
    current_stock = db.Column(db.Integer, default=0)
    ensemble_id = db.Column(db.Integer, db.ForeignKey('ensemble.id'), nullable=False)
    
    ensemble = db.relationship('Ensemble', backref='records')
    
    def __repr__(self):
        return f'<Record {self.catalog_number} - {self.title}>'
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
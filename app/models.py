from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

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

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

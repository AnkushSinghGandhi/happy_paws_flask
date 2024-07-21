from app import db
from datetime import datetime

class NGO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone_no = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    dogs = db.relationship('Dog', backref='ngo', lazy=True)
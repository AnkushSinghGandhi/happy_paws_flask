from app import db
from datetime import datetime

class Feeder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone_no = db.Column(db.String(20), nullable=False)
    friends = db.Column(db.PickleType, nullable=True)
    status = db.Column(db.String(120), nullable=True)
    help = db.Column(db.String(120), nullable=True)
    dogs = db.relationship('Dog', backref='feeder', lazy=True)
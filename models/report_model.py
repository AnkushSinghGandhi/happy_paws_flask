from app import db
from datetime import datetime

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=True)
    location = db.Column(db.String(120), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    dog_id = db.Column(db.Integer, db.ForeignKey('dog.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

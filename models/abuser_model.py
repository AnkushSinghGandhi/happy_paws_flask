from app import db
from datetime import datetime

class DogAbuser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(120), nullable=True)
    media = db.Column(db.PickleType, nullable=True)
    name = db.Column(db.String(80), nullable=False)
    contact = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(120), nullable=True)
    reported_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    incident_level = db.Column(db.String(120), nullable=True)
    date_of_case = db.Column(db.DateTime, default=datetime.utcnow)

    def as_dict(self):
        return {
            'id': self.id,
            'photo': self.photo,
            'media': self.media,
            'name': self.name,
            'contact': self.contact,
            'reported_by': self.reported_by,
            'incident_level': self.incident_level,
            'date_of_case': self.date_of_case
        }
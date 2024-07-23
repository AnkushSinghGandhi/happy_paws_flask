from app import db
from datetime import datetime

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    photos = db.Column(db.PickleType, nullable=True)
    videos = db.Column(db.PickleType, nullable=True)
    locations = db.Column(db.PickleType, nullable=True)
    tags = db.Column(db.PickleType, nullable=True)
    behavior = db.Column(db.String(120), nullable=True)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow)
    vaccine = db.Column(db.Boolean, default=False)
    feeder_id = db.Column(db.Integer, db.ForeignKey('feeder.id'), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    breed = db.Column(db.String(80), nullable=True)
    lost = db.Column(db.Boolean, default=False)
    treatment_req = db.Column(db.Boolean, default=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'photos': self.photos,
            'videos': self.videos,
            'locations': self.locations,
            'tags': self.tags,
            'behavior': self.behavior,
            'updated_on': self.updated_on,
            'vaccine': self.vaccine,
            'feeder_id': self.feeder_id,
            'age': self.age,
            'breed': self.breed,
            'lost': self.lost,
            'treatment_req': self.treatment_req,
            'owner_id': self.owner_id
        }

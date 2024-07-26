from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(120), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(120), nullable=True)

    def as_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'points': self.points,
            'description': self.description
        }

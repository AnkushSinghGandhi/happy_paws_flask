from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')
    dogs = db.relationship('Dog', backref='owner', lazy=True)

    def as_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role,
            'dogs': [dog.as_dict() for dog in self.dogs]
        }
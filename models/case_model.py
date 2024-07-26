from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    abuser_id = db.Column(db.Integer, db.ForeignKey('dog_abuser.id'), nullable=False)
    dog_id = db.Column(db.Integer, db.ForeignKey('dog.id'), nullable=False)
    status = db.Column(db.String(120), nullable=True)

    def as_dict(self):
        return {
            'id': self.id,
            'abuser_id': self.abuser_id,
            'dog_id': self.dog_id,
            'status': self.status
        }
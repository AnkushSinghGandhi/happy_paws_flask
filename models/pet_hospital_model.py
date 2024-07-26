from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PetHospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone_no = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'phone_no': self.phone_no,
            'email': self.email
        }

from app import db
from datetime import datetime

class PawsWallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    points = db.Column(db.Integer, default=0)
    transactions = db.relationship('Transaction', backref='wallet', lazy=True)

    def as_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'points': self.points,
            'transactions': [transaction.as_dict() for transaction in self.transactions]
        }

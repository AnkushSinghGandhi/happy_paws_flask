from flask import request, jsonify
from models import PawsWallet, Transaction, db

def get_wallet(user_id):
    wallet = PawsWallet.query.filter_by(user_id=user_id).first()
    if not wallet:
        return jsonify({'message': 'Wallet not found'}), 404
    return jsonify(wallet.as_dict()), 200

def create_transaction():
    data = request.get_json()
    new_transaction = Transaction(
        type=data['type'],
        points=data['points'],
        user_id=data['user_id']
    )
    db.session.add(new_transaction)

    wallet = PawsWallet.query.filter_by(user_id=data['user_id']).first()
    if wallet:
        wallet.points += data['points']
    else:
        wallet = PawsWallet(user_id=data['user_id'], points=data['points'])
        db.session.add(wallet)

    db.session.commit()
    return jsonify({'message': 'Transaction created successfully'}), 201

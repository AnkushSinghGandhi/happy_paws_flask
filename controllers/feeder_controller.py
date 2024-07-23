from flask import request, jsonify
from models import Feeder, db

def get_feeder(id):
    feeder = Feeder.query.get(id)
    if not feeder:
        return jsonify({'message': 'Feeder not found'}), 404
    return jsonify(feeder.as_dict()), 200

def create_feeder():
    data = request.get_json()

    new_feeder = Feeder(
        name=data['name'],
        address=data['address'],
        phone_no=data['phone_no'],
        friends=data['friends'],
        status=data['status'],
        help=data['help']
    )
    db.session.add(new_feeder)
    db.session.commit()

    return jsonify({'message': 'Feeder registered successfully'}), 201

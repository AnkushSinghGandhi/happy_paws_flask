from flask import request, jsonify
from models import NGO, db

def get_ngos():
    ngos = NGO.query.all()
    return jsonify([ngo.as_dict() for ngo in ngos]), 200

def create_ngo():
    data = request.get_json()
    new_ngo = NGO(
        name=data['name'],
        address=data['address'],
        phone_no=data['phone_no'],
        email=data['email']
    )
    db.session.add(new_ngo)
    db.session.commit()
    return jsonify({'message': 'NGO registered successfully'}), 201

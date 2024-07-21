from flask import request, jsonify
from flask_jwt_extended import jwt_required
from models import Dog, db

@jwt_required()
def get_dogs():
    dogs = Dog.query.all()
    return jsonify([dog.as_dict() for dog in dogs]), 200

@jwt_required()
def get_dog(id):
    dog = Dog.query.get(id)
    if not dog:
        return jsonify({'message': 'Dog not found'}), 404
    return jsonify(dog.as_dict()), 200

@jwt_required()
def create_dog():
    data = request.get_json()

    new_dog = Dog(
        name=data['name'],
        gender=data['gender'],
        photos=data['photos'],
        videos=data['videos'],
        locations=data['locations'],
        tags=data['tags'],
        behavior=data['behavior'],
        vaccine=data['vaccine'],
        feeder_id=data['feeder_id'],
        age=data['age'],
        breed=data['breed'],
        lost=data['lost'],
        treatment_req=data['treatment_req'],
        owner_id=data['owner_id']
    )
    db.session.add(new_dog)
    db.session.commit()

    return jsonify({'message': 'Dog registered successfully'}), 201

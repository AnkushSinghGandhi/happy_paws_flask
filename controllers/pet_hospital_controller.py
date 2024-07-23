from flask import request, jsonify
from models import PetHospital, db

def get_pet_hospitals():
    pet_hospitals = PetHospital.query.all()
    return jsonify([hospital.as_dict() for hospital in pet_hospitals]), 200

def create_pet_hospital():
    data = request.get_json()
    new_pet_hospital = PetHospital(
        name=data['name'],
        address=data['address'],
        phone_no=data['phone_no'],
        email=data['email']
    )
    db.session.add(new_pet_hospital)
    db.session.commit()
    return jsonify({'message': 'Pet Hospital registered successfully'}), 201

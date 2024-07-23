from flask import request, jsonify
from models import Case, db

def get_cases():
    cases = Case.query.all()
    return jsonify([case.as_dict() for case in cases]), 200

def create_case():
    data = request.get_json()
    new_case = Case(
        abuser_id=data['abuser_id'],
        dog_id=data['dog_id'],
        status=data['status']
    )
    db.session.add(new_case)
    db.session.commit()
    return jsonify({'message': 'Case created successfully'}), 201

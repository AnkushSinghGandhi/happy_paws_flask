from flask import request, jsonify
from models import Report, db

def get_reports():
    reports = Report.query.all()
    return jsonify([report.as_dict() for report in reports]), 200

def create_report():
    data = request.get_json()
    new_report = Report(
        type=data['type'],
        description=data['description'],
        location=data['location'],
        dog_id=data['dog_id'],
        user_id=data['user_id']
    )
    db.session.add(new_report)
    db.session.commit()
    return jsonify({'message': 'Report created successfully'}), 201

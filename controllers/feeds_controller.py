from flask import jsonify
from models.report_model import Report
from models.dog_model import Dog

def get_feeds():
    reports = Report.query.order_by(Report.timestamp.desc()).limit(10).all()
    lost_dogs = Dog.query.filter_by(lost=True).order_by(Dog.updated_on.desc()).limit(10).all()
    
    feeds = {
        'reports': [report.as_dict() for report in reports],
        'lost_dogs': [dog.as_dict() for dog in lost_dogs]
    }
    
    return jsonify(feeds), 200

from flask import Blueprint
from routes.dog_routes import dog_bp
from routes.user_routes import user_bp
from routes.feeds_routes import feeds_bp
from routes.feeder_routes import feeder_bp
from routes.ngo_routes import ngo_bp
from routes.pet_hospital_routes import pet_hospital_bp
from routes.report_routes import report_bp
from routes.reward_routes import reward_bp
from routes.paws_wallet_routes import paws_wallet_bp
from routes.case_routes import case_bp

def register_routes(app):
    app.register_blueprint(dog_bp, url_prefix='/dogs')
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(feeds_bp, url_prefix='/feeds')
    app.register_blueprint(feeder_bp, url_prefix='/feeders')
    app.register_blueprint(ngo_bp, url_prefix='/ngos')
    app.register_blueprint(pet_hospital_bp, url_prefix='/pet_hospitals')
    app.register_blueprint(report_bp, url_prefix='/reports')
    app.register_blueprint(reward_bp, url_prefix='/rewards')
    app.register_blueprint(paws_wallet_bp, url_prefix='/paws_wallet')
    app.register_blueprint(case_bp, url_prefix='/cases')

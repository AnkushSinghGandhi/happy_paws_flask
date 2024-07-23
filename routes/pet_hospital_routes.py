from flask import Blueprint
from controllers.pet_hospital_controller import get_pet_hospitals, create_pet_hospital

pet_hospital_bp = Blueprint('pet_hospital_bp', __name__)

pet_hospital_bp.route('/', methods=['GET'])(get_pet_hospitals)
pet_hospital_bp.route('/', methods=['POST'])(create_pet_hospital)

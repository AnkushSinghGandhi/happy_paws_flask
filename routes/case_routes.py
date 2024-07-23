from flask import Blueprint
from controllers.case_controller import get_cases, create_case

case_bp = Blueprint('case_bp', __name__)

case_bp.route('/', methods=['GET'])(get_cases)
case_bp.route('/', methods=['POST'])(create_case)

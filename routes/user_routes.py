from flask import Blueprint
from controllers.user_controller import create_user, login_user

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/signup', methods=['POST'])(create_user)
user_bp.route('/login', methods=['POST'])(login_user)

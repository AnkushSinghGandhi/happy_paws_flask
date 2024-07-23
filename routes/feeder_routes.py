from flask import Blueprint
from controllers.feeder_controller import get_feeder, create_feeder

feeder_bp = Blueprint('feeder_bp', __name__)

feeder_bp.route('/<int:id>', methods=['GET'])(get_feeder)
feeder_bp.route('/', methods=['POST'])(create_feeder)

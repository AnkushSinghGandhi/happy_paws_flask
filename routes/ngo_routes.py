from flask import Blueprint
from controllers.ngo_controller import get_ngos, create_ngo

ngo_bp = Blueprint('ngo_bp', __name__)

ngo_bp.route('/', methods=['GET'])(get_ngos)
ngo_bp.route('/', methods=['POST'])(create_ngo)

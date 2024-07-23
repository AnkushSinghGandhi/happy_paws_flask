from flask import Blueprint
from controllers.feeds_controller import get_feeds

feeds_bp = Blueprint('feeds_bp', __name__)

feeds_bp.route('/', methods=['GET'])(get_feeds)

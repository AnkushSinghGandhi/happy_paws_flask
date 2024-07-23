from flask import Blueprint
from controllers.report_controller import get_reports, create_report

report_bp = Blueprint('report_bp', __name__)

report_bp.route('/', methods=['GET'])(get_reports)
report_bp.route('/', methods=['POST'])(create_report)

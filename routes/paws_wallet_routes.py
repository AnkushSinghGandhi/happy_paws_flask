from flask import Blueprint
from controllers.paws_wallet_controller import get_wallet, create_transaction

paws_wallet_bp = Blueprint('paws_wallet_bp', __name__)

paws_wallet_bp.route('/<int:user_id>', methods=['GET'])(get_wallet)
paws_wallet_bp.route('/transaction', methods=['POST'])(create_transaction)

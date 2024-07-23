from flask import Blueprint
from controllers.reward_controller import get_rewards, create_reward

reward_bp = Blueprint('reward_bp', __name__)

reward_bp.route('/', methods=['GET'])(get_rewards)
reward_bp.route('/', methods=['POST'])(create_reward)

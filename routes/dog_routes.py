from flask import Blueprint
from controllers.dog_controller import get_dogs, get_dog, create_dog

dog_bp = Blueprint('dog_bp', __name__)

dog_bp.route('/', methods=['GET'])(get_dogs)
dog_bp.route('/<int:id>', methods=['GET'])(get_dog)
dog_bp.route('/', methods=['POST'])(create_dog)

from flask import request, jsonify
from models import Reward, db

def get_rewards():
    rewards = Reward.query.all()
    return jsonify([reward.as_dict() for reward in rewards]), 200

def create_reward():
    data = request.get_json()
    new_reward = Reward(
        type=data['type'],
        points=data['points'],
        description=data['description']
    )
    db.session.add(new_reward)
    db.session.commit()
    return jsonify({'message': 'Reward created successfully'}), 201

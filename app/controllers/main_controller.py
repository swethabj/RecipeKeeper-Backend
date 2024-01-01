# app/controllers/main_controller.py

from flask import Blueprint, jsonify

main_controller = Blueprint('main_controller', __name__)

@main_controller.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to your Flask project!'})

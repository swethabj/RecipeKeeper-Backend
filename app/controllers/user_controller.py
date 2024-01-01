from flask import Blueprint, request, jsonify
from app import db , bcrypt  # Import db directly from the app package
from app.models.user_model import User


user_controller = Blueprint('user_controller', __name__)

# #List All Users from users table 
# @user_controller.route('/users', methods=['GET'])
# def get_users():
#     users = User.query.all()
#     users_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
#     return jsonify(users_list)

# #GET User By ID from users table 
# @user_controller.route('/users/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     user = User.query.get_or_404(user_id)
#     return jsonify({'id': user.id, 'username': user.username, 'email': user.email})

#Insert User Data into users table 
@user_controller.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    # Check if the User , Email already exists
    existing_user = User.query.filter_by(username=data['username']).first()
    existing_email = User.query.filter_by(email_address=data['email']).first()
    if existing_user and existing_email:
        return jsonify({'message': 'User and Email already exists, Please try different username and emailaddress'}), 409  # HTTP status code 409 for conflict
    elif existing_user:
        return jsonify({'message': 'User already exists, Please try different username'}), 409  # HTTP status code 409 for conflict
    elif existing_email:
        return jsonify({'message': 'Email already exists, Please try different emailaddress'}), 409  # HTTP status code 409 for conflict
    else:
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

        new_user = User(username=data['username'],  #DB_Name = #Ap_pName
                        email_address=data['email'], 
                        password_hash=hashed_password,
                        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'id': new_user.id,
                        'username': new_user.username,
                        'email': new_user.email_address}), 201

# #Update User Data in users table 
# @user_controller.route('/users/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     user = User.query.get_or_404(user_id)
#     data = request.get_json()
#     user.username = data['username']
#     user.email = data['email']
#     db.session.commit()
#     return jsonify({'id': user.id, 'username': user.username, 'email': user.email})

# #Delete User Data by user id 
# @user_controller.route('/users/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
#     user = User.query.get_or_404(user_id)
#     db.session.delete(user)
#     db.session.commit()
#     return jsonify({'message': 'User deleted successfully'})

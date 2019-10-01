from flask import Blueprint, jsonify, request

from DBUtil.User import UserDAO

# blueprint declaration
userAPI = Blueprint('userAPI', __name__)
userDB = UserDAO()

@userAPI.route('/user/login', methods=['POST'])
def login_user_details():
    if request.method =='POST':
        try:
            result= userDB.user_AWSLogin(request.get_json())
            return jsonify({"data":result})
        except Exception as e:
            return jsonify({"message": str(e), "status": "failed"}), 404

@userAPI.route('/update/user_first_time/password', methods=['PUT'])
def update_first_time_password():
    if request.method =='PUT':
        try:
            result= userDB.update_aws_first_time_password(request.get_json())
            return jsonify({"data":result})
        except Exception as e:
            return jsonify({"message": str(e), "status": "failed"}), 404

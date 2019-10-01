'''
Created on May 16, 2019

@author: Shyamjin
'''
from flask import Blueprint, jsonify, request

from DBUtil.Student import StudentDAO

# blueprint declaration
studentAPI = Blueprint('studentAPI', __name__)
studentDB = StudentDAO()
@studentAPI.route('/add/service' ,methods=['POST'])
def add_student():
    if request.method =='POST':
        try:
            studentDB.post_student(request.get_json())
            return jsonify({"message": "Service has been added successfully", "status": "success"}), 200
        except Exception as e:
            return jsonify({"message": str(e), "status": "failed"}), 404


@studentAPI.route('/update/service/<id>',methods=['PUT'])
def update_student_by_id(id):
    try:
        data = request.get_json()
        result = studentDB.udpate_student(id,data)
        return jsonify({"message": "Service has been updated successfully with {}".format(id), "status": "success"}), 200

    except Exception as e:
        return jsonify({"message": str(e), "status": "failed"}), 404


@studentAPI.route('/delete/service/<id>',methods=['DELETE'])
def delete_student_by_id(id):
    try:
        studentData= studentDB.deleteStudentById(id)
        return jsonify({"Data": studentData, "status": "success"}), 200
    except Exception as e:
        return jsonify({"message": str(e), "status": "failed"}), 404
        
@studentAPI.route('/get/service/<id>',methods=['GET'])
def get_student_by_id(id):
    try:
        studentData= studentDB.studentById(id)
        return jsonify({"Data": studentData, "status": "success"}), 200
    except Exception as e:
        return jsonify({"message": str(e), "status": "failed"}), 404




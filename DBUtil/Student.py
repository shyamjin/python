from models.Student import Student
from DBUtil.base import  Session
import json


def serialize(cls):
    class A(object):
        pass

    _excluded_keys = set(A.__dict__.keys())  # Get all default class atributes
    _excluded_keys.add("_sa_instance_state")  # Special attributes
    data = {}
    for (key, value) in cls.__dict__.items():
        if key in _excluded_keys: continue
        if type(value) == set: value = list(value)
        data[key] = value
    return data
class StudentDAO():

    def post_student(self,studentData):
        print(studentData)
        '''
          General description:
          Args:
             no Args
          Returns:
                  create Database entities in the Students table.
          Example :
          get_student()
        '''
        session = Session()
        try:
            studentData = Student(studentData["service_name"])
            result = session.add(studentData)
        except Exception as e:
            return "can not add somthing is going wrong with exception- {}".format(str(e))
        finally:
            session.commit()
        return result
    def udpate_student(self,studentId,data):
        session = Session()
        try:
            temp = {}
            for key,values in data.items():
                temp[key]=values

            updateData= session.query(Student).filter(Student.id==studentId).update(temp)
            session.commit()
            return "records has been updated succesfully with for {}".format(updateData)
        except Exception as e:
            return "Records can not be updated due to {}".format(str(e))

    def studentById(self,studentID):
        session = Session()
        try:
            StudentOutput =session.query(Student).filter(Student.id==studentID).first()
            return serialize(StudentOutput)

        except Exception as e:
            return "Record not found with that id {}".format(studentID)
  
    def deleteStudentById(self,studentID):
        session = Session()
        try:
            StudentOutput =session.query(Student).filter(Student.id==studentID).delete()
            session.commit()
            return "records has been deleted succesfully with for id - {}".format(studentID)

        except Exception as e:
            return "Record not found with that id {}".format(studentID)




'''
Created on May 16, 2019

@author: shyamjin
'''

from flask import Flask
import os
from modules import StudentAPI, UserAPI
#from elasticsearch import Elasticsearch

application = Flask(__name__, static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), './static'))
#application.elasticsearch = Elasticsearch(['http://localhost:5050'])
application.register_blueprint(StudentAPI.studentAPI)
application.register_blueprint(UserAPI.userAPI)

if __name__ == '__main__':
    application.run(debug=True,port=8000, host='0.0.0.0')

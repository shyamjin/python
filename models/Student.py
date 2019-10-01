from sqlalchemy import Column, Integer, String,Sequence
from DBUtil.base import  Base
USER_ID_SEQ = Sequence('servicesid_seq')  
class Student(Base):
    __tablename__ = 'services'
    id = Column(Integer,USER_ID_SEQ, primary_key=True,server_default=USER_ID_SEQ.next_value())
    service_name = Column(String)

    def __init__(self,service_name):
        self.service_name = service_name


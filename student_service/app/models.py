from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    enrollment_no=Column(String, unique=True,index=True,nullable=False)
    name=Column(String, nullable=False)
    email=Column(String, unique=True, nullable=False)
    phone=Column(String, nullable=False)
    address=Column(String, nullable=False)
    course_id=Column(Integer, nullable=False)
    subject_code=Column(String, nullable=False)
    enrolled_at=Column(DateTime,default=datetime.utcnow)
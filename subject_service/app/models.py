from sqlalchemy import Column, Integer, String
from .database import Base

class Subject(Base):
    __tablename__ = "subjects"

    id=Column(Integer, primary_key=True, index=True)
    subject_code=Column(String, unique=True,index=True)
    subject_name=Column(String, nullable=False)
    marks=Column(Integer)
    course_id=Column(Integer)
    
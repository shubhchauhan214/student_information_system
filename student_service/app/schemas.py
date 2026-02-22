from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class StudentCreate(BaseModel):
    enrollment_no: str
    name: str
    email:EmailStr
    phone:Optional[str]=None
    address: Optional[str]=None
    course_id: int
    subject_code: str

class StudentUpdate(BaseModel):
    name: Optional[str]=None
    email:Optional[EmailStr]=None
    phone:Optional[str]=None
    address:Optional[str]=None
    course_id:Optional[int]=None
    subject_code:Optional[str]=None

class StudentResponse(BaseModel):
    id: int
    enrollment_no: str
    name: str
    email:EmailStr
    phone:Optional[str]=None
    address: Optional[str]=None
    course_id: int
    subject_code: str

    class Config:
        from_attribute=True
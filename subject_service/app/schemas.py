from pydantic import BaseModel
from typing import Optional

class SubjectCreate(BaseModel):
    subject_code: str
    subject_name: str
    marks: int
    course_id: int

class SubjectUpdate(BaseModel):
    subject_code: Optional[str]=None
    subject_name:Optional[str]=None
    marks: Optional[str]=None
    course_id: Optional[int]=None

class SubjectResponse(BaseModel):
    id: int

    class Config:
        from_attributes = True
from pydantic import BaseModel
from typing import Optional

class CourseCreate(BaseModel):
    name: str
    duration: str

class CourseUpdate(BaseModel):
    name: Optional[str]=None
    duration: Optional[str]=None

class CourseResponse(BaseModel):
    id: int
    name: str
    duration: str
    
    class Config:
        from_attributes = True
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from app import crud, schemas

router = APIRouter(prefix="/course", tags=["Courses"])

@router.post("/", response_model=schemas.CourseResponse)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    try:
        new_course = crud.create_course(db, course)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if not new_course:
        raise HTTPException(status_code=404, detail="Course not found.")
    
    return new_course
    

@router.get("/", response_model=list[schemas.CourseResponse])
def read_courses(db: Session=Depends(get_db)):
    courses = crud.get_all_courses(db)
    return courses

@router.get("/{course_id}", response_model=schemas.CourseResponse)
def read_course(course_id: int, db: Session=Depends(get_db)):
    course = crud.get_course_by_id(db, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.put("/{course_id}", response_model=schemas.CourseResponse)
def update_course(course_id: int, course:schemas.CourseUpdate, db: Session=Depends(get_db)):
    updated_course = crud.update_course(db, course_id, course)
    if not updated_course:
        raise HTTPException(status_code=404, detail="Course not found")
    return updated_course

@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session=Depends(get_db)):
    deleted_course=crud.delete_course(db, course_id)
    if not deleted_course:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"message": "Deleted successfully"}


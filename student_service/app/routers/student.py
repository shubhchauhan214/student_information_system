from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/", response_model=schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_student(db, student)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[schemas.StudentResponse])
def get_all_students(db: Session = Depends(get_db)):
    return crud.get_all_students(db)

@router.get("/{enrollment_no}", response_model=schemas.StudentResponse)
def get_student(enrollment_no: str, db: Session = Depends(get_db)):
    student = crud.get_student_by_enrollment(db, enrollment_no)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/{enrollment_no}", response_model=schemas.StudentResponse)
def update_student(enrollment_no: str, student_update: schemas.StudentUpdate, db: Session = Depends(get_db)):
    try:
        updated = crud.update_student(db, enrollment_no, student_update)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated

@router.delete("/{enrollment_no}")
def delete_student(enrollment_no: str, db: Session = Depends(get_db)):
    deleted = crud.delete_student(db, enrollment_no)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": f"Student {enrollment_no} deleted successfully"}
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from app import crud, schemas

router = APIRouter(prefix="/subjects", tags=["Subjects"])

@router.post("/", response_model = schemas.SubjectResponse)
def create_subject(subject: schemas.SubjectCreate, db: Session = Depends(get_db)):
    
    new_subject =crud.create_subject(db, subject)

    if not new_subject:
        raise HTTPException(status_code=400, detail="Invalid course_id")

@router.get("/", response_model=list[schemas.SubjectResponse])
def get_subjects(db: Session=Depends(get_db)):
    subjects = crud.get_all_subjects(db)
    return subjects

@router.get("/{subject_code}", response_model=schemas.SubjectResponse)
def get_subject(subject_code: str, db: Session=Depends(get_db)):
    subject = crud.get_subject_by_id(db, subject_code)
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return subject

@router.put("/{subject_code}", response_model=schemas.SubjectResponse)
def update_subject(subject_code: str, subject:schemas.SubjectUpdate, db: Session=Depends(get_db)):
    updated_subject = crud.update_subject(db, subject_code, subject)
    if not updated_subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return updated_subject

@router.delete("/{subject_code}")
def delete_subject(subject_code: str, db: Session=Depends(get_db)):
    deleted_subject=crud.delete_subject(db, subject_code)
    if not deleted_subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return {"message": "Deleted Successfully"}


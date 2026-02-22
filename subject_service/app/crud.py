from sqlalchemy.orm import Session
from . import models, schemas
import httpx

def validate_course(course_id:int):

    url =f"http://127.0.0.1:8000/course/{course_id}"

    try:
        response=httpx.get(url)

        if response.status_code==200:
            return True
        else:
            return False
    
    except Exception:
        return False

def create_subject(db: Session, subject: schemas.SubjectCreate):

    if not validate_course(subject.course_id):
        return None
    
    db_subject = models.Subject(**subject.dict())
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject


def get_all_subjects(db: Session):
    return db.query(models.Subject).all()

def get_subject_by_id(db: Session, subject_code: str):
    return db.query(models.Subject).filter(models.Subject.subject_code == subject_code).first()

def update_subject(db: Session, subject_code: str, subject_update: schemas.SubjectUpdate):

    db_subject = db.query(models.Subject).filter(
        models.Subject.subject_code == subject_code
    ).first()

    if not db_subject:
        return None

    update_data = subject_update.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_subject, key, value)

    db.commit()
    db.refresh(db_subject)

    return db_subject

def delete_subject(db: Session, subject_code: str):
    db_subject=db.query(models.Subject).filter(models.Subject.subject_code==subject_code).first()

    if not db_subject:
        return None
    
    db.delete(db_subject)
    db.commit()

    return db_subject


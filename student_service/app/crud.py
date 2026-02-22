import httpx
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import models, schemas

def validate_course(course_id: int):
    try:
        response=httpx.get(f"http://127.0.0.1:8000/course/{course_id}")
        return response.status_code==200
    except Exception:
        return False

def validate_subject(subject_code: str):
    try:
        response=httpx.get(f"http://127.0.0.1:8001/subjects/{subject_code}")
        return response.status_code==200
    except Exception:
        return False
    
def create_student(db:Session, student=schemas.StudentCreate):
    if not validate_course(student.course_id):
        raise ValueError("Invalid course_id")
    if not validate_subject(student.subject_code):
        raise ValueError("Invalid subject_code")
    
    db_student=models.Student(**student.dict())
    db.add(db_student)

    try:
        db.commit()
        db.refresh(db_student)
        return db_student
    except IntegrityError:
        db.rollback()
        raise ValueError("Student with this enrollment_no or email already exists")
    
def get_all_students(db: Session):
    return db.query(models.Student).all()

def get_student_by_enrollment(db: Session, enrollment_no: str):
    return db.query(models.Student).filter(models.Student.enrollment_no==enrollment_no).first()


def update_student(db: Session, enrollment_no: str, student_update: schemas.StudentUpdate):
    db_student=db.query(models.Student).filter(models.Student.enrollment_no==enrollment_no).first()

    if not db_student:
        return None
    
    if student_update.course_id:
        if not validate_course(student_update.course_id):
            raise ValueError("Invalid course_id")
        
    if student_update.subject_code:
        if not validate_subject(student_update.subject_code):
            raise ValueError("Invalid subject_code")
        
    update_data = student_update.dict(exclude_unset=True, exclude_none=True)
    for key, value in update_data.items():
        setattr(db_student, key, value)

    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, enrollment_no: str):
    db_student=db.query(models.Student).filter(models.Student.enrollment_no==enrollment_no).first()

    if not db_student:
        return None
    
    db.delete(db_student)
    db.commit()
    return db_student

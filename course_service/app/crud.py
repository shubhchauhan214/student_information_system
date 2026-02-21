from sqlalchemy.orm import Session
from .models import Course

def create_course(db: Session, name: str, duration: str):
    course = Course(name=name, duration=duration)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

def get_all_courses(db: Session):
    return db.query(Course).all()

def get_course_by_id(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()

def update_course(db: Session, course_id: int, name: str, duration: str):
    course = db.query(Course).filter(Course.id == course_id).first()
    if course:
        course.name = name
        course.duration = duration
        db.commit()
        db.refresh(course)
    return course

def delete_course(db: Session, course_id: int):
    course = db.query(Course).filter(Course.id == course_id).first()
    if course:
        db.delete(course)
        db.commit()
    return course


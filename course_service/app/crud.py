from sqlalchemy.orm import Session
from . import models, schemas

def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_all_courses(db: Session):
    return db.query(models.Course).all()

def get_course_by_id(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()

def update_course(db: Session, course_id: int, course_update:schemas.CourseUpdate):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not db_course:
        return None
    
    update_data = course_update.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_course, key, value)

        db.commit()
        db.refresh(db_course)
        return db_course

def delete_course(db: Session, course_id: int):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if db_course:
        db.delete(db_course)
        db.commit()
    return db_course


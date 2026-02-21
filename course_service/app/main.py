from fastapi import FastAPI
from .database import Base, engine
from .routers import course

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Course Service")

app.include_router(course.router)
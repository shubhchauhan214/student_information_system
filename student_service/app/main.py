from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routers import student

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Service")

app.include_router(student.router)
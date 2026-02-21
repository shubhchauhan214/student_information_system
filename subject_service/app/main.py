from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routers import subject

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Subject Service")

app.include_router(subject.router)
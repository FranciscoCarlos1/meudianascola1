import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine, SessionLocal
from . import models
from .seed import seed_admin
from .routers import auth as auth_router, students, classes, attendance, grades

app = FastAPI(title="Meu Dia na Escola API")

origins = os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables and seed admin
Base.metadata.create_all(bind=engine)
with SessionLocal() as db:
    seed_admin(db)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(auth_router.router)
app.include_router(students.router)
app.include_router(classes.router)
app.include_router(attendance.router)
app.include_router(grades.router)

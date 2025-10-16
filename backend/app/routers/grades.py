from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..schemas import GradeIn, GradeOut
from ..auth import get_current_user

router = APIRouter(prefix="/grades", tags=["grades"])

@router.get("/{student_id}", response_model=list[GradeOut])
def list_grades(student_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(models.Grade).filter(models.Grade.student_id == student_id).all()

@router.post("/", response_model=GradeOut)
def add_grade(payload: GradeIn, db: Session = Depends(get_db), user=Depends(get_current_user)):
    g = models.Grade(**payload.model_dump())
    db.add(g); db.commit(); db.refresh(g)
    return g

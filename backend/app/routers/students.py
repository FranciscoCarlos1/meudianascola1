from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..schemas import StudentIn, StudentOut
from ..auth import get_current_user

router = APIRouter(prefix="/students", tags=["students"])

@router.get("/", response_model=list[StudentOut])
def list_students(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(models.Student).all()

@router.post("/", response_model=StudentOut)
def create_student(payload: StudentIn, db: Session = Depends(get_db), user=Depends(get_current_user)):
    st = models.Student(**payload.model_dump())
    db.add(st)
    db.commit(); db.refresh(st)
    return st

@router.put("/{student_id}", response_model=StudentOut)
def update_student(student_id: int, payload: StudentIn, db: Session = Depends(get_db), user=Depends(get_current_user)):
    st = db.query(models.Student).get(student_id)
    if not st:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    for k, v in payload.model_dump().items():
        setattr(st, k, v)
    db.commit(); db.refresh(st)
    return st

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    st = db.query(models.Student).get(student_id)
    if not st:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    db.delete(st); db.commit()
    return {"ok": True}

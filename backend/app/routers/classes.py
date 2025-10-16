from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..schemas import ClassIn, ClassOut
from ..auth import get_current_user

router = APIRouter(prefix="/classes", tags=["classes"])

@router.get("/", response_model=list[ClassOut])
def list_classes(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(models.SchoolClass).all()

@router.post("/", response_model=ClassOut)
def create_class(payload: ClassIn, db: Session = Depends(get_db), user=Depends(get_current_user)):
    c = models.SchoolClass(**payload.model_dump())
    db.add(c); db.commit(); db.refresh(c)
    return c

@router.put("/{class_id}", response_model=ClassOut)
def update_class(class_id: int, payload: ClassIn, db: Session = Depends(get_db), user=Depends(get_current_user)):
    c = db.query(models.SchoolClass).get(class_id)
    if not c:
        raise HTTPException(status_code=404, detail="Turma não encontrada")
    for k, v in payload.model_dump().items():
        setattr(c, k, v)
    db.commit(); db.refresh(c)
    return c

@router.delete("/{class_id}")
def delete_class(class_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    c = db.query(models.SchoolClass).get(class_id)
    if not c:
        raise HTTPException(status_code=404, detail="Turma não encontrada")
    db.delete(c); db.commit()
    return {"ok": True}

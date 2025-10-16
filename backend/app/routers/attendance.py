from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..schemas import AttendanceIn
from ..auth import get_current_user

router = APIRouter(prefix="/attendance", tags=["attendance"])

@router.get("/{class_id}")
def get_attendance(class_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(models.Attendance).filter(models.Attendance.class_id == class_id).all()

@router.post("/")
def mark_attendance(payload: AttendanceIn, db: Session = Depends(get_db), user=Depends(get_current_user)):
    a = models.Attendance(**payload.model_dump())
    db.add(a); db.commit(); db.refresh(a)
    return {"id": a.id}

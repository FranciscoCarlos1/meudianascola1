from pydantic import BaseModel, EmailStr
from datetime import date, datetime

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: str
    class Config:
        from_attributes = True

class StudentIn(BaseModel):
    name: str
    cpf: str
    birthdate: date | None = None
    phone: str | None = None
    email: str | None = None

class StudentOut(StudentIn):
    id: int
    class Config:
        from_attributes = True

class ClassIn(BaseModel):
    name: str
    year: int | None = None

class ClassOut(ClassIn):
    id: int
    class Config:
        from_attributes = True

class EnrollmentIn(BaseModel):
    student_id: int
    class_id: int

class AttendanceIn(BaseModel):
    student_id: int
    class_id: int
    date: date
    status: str

class GradeIn(BaseModel):
    student_id: int
    class_id: int
    subject: str
    score: int

class GradeOut(GradeIn):
    id: int
    date_recorded: datetime
    class Config:
        from_attributes = True

from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, Text, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String, default="admin")  # admin | teacher | staff

class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    cpf: Mapped[str] = mapped_column(String, unique=True, index=True)
    birthdate: Mapped[Date | None]
    phone: Mapped[str | None]
    email: Mapped[str | None]

class SchoolClass(Base):
    __tablename__ = "classes"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    year: Mapped[int | None]

class Enrollment(Base):
    __tablename__ = "enrollments"
    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    UniqueConstraint("student_id", "class_id")
    student = relationship("Student")
    klass = relationship("SchoolClass")

class Attendance(Base):
    __tablename__ = "attendance"
    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    date: Mapped[Date]
    status: Mapped[str] = mapped_column(String)  # present | absent | late
    UniqueConstraint("student_id", "class_id", "date")

class Grade(Base):
    __tablename__ = "grades"
    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    subject: Mapped[str] = mapped_column(String)
    score: Mapped[Integer]
    date_recorded: Mapped[DateTime] = mapped_column(default=datetime.utcnow)

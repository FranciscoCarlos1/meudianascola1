from sqlalchemy.orm import Session
from .models import User
from .auth import get_password_hash
import os

def seed_admin(db: Session):
    admin_email = os.getenv("ADMIN_EMAIL", "admin@escola.local")
    admin_password = os.getenv("ADMIN_PASSWORD", "admin123")
    existing = db.query(User).filter(User.email == admin_email).first()
    if not existing:
        user = User(email=admin_email, hashed_password=get_password_hash(admin_password), role="admin")
        db.add(user)
        db.commit()

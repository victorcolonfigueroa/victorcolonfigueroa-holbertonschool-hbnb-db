"""
User related functionality
"""
from src import db
from src.models.base import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

class User(db.Model):
    """User representation"""

    id = db.Column(db.String(36), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # Ensure secure storage
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())

    def __init__(self, email: str, password: str, is_admin: bool = False):
        self.id = str(uuid.uuid4())
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def __repr__(self) -> str:
        return f"<User {self.id} {(self.email)}>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "email": self.email,
            # "password": self.password,  # Never expose password
            "is_admin": self.is_admin
        }

    def create(self):
        """Create a new user"""
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        """Update an existing user"""
        db.session.commit()
        return self
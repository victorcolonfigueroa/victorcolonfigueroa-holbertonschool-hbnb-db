"""
Country related functionality
"""
<<<<<<< Updated upstream
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

__tablename__ = 'countries'

id = Column(Integer, primary_key=True)
name = Column(String, nullable=False)
code = Column(String, nullable=False, unique=False)


class Country(Base):
    """
    Country representation

    This class does NOT inherit from Base, you can't delete or update a country

    This class is used to get and list countries
    """

    name: str
    code: str
    cities: list
=======
from src import db
from src.models.base import Base

class Country(Base):
    name = db.Column(db.String(120), nullable=False)
    code = db.Column(db.String(2), nullable=False)
    cities = db.relationship('City', backref='country', lazy=True)
>>>>>>> Stashed changes

    def __init__(self, name: str, code: str, **kw) -> None:
        super().__init__(**kw)
        self.name = name
        self.code = code

    def __repr__(self) -> str:
        return f"<Country {self.name} {self.code}>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code
        }

    def create(self):
        """Create a new country"""
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        """Update an existing country"""
        db.session.commit()
        return self


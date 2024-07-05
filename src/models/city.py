"""
City related functionality
"""
from src import db
from src.models.base import Base
from src.models.country import Country
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.models.base import Base


class City(Base):
    __tablename__ = 'cities'
    
    id = Column(Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    country_code = db.Column(db.String(36), db.ForeignKey('countries.id'), nullable=False)
    created_at = Column(DateTime(timezome=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    country = relationship("Country", back_populates="cities")
    
    def __init__(self, name: str, country_code: str, **kw) -> None:
        super().__init__(**kw)
        self.name = name
        self.country_code = country_code

    def __repr__(self) -> str:
        return f"<City {self.name} {self.country_code}>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "country_code": self.country_code
        }

    def create(self):
        """Create a new city"""
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        """Update an existing city"""
        db.session.commit()
        return self
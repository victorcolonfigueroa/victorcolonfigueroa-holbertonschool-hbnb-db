"""
Place related functionality
"""
from src import db
from src.models.base import Base
from src.models.city import City
from src.models.user import User
from sqlalchemy import Column, String, Float, Integer, ForeignKey

__tablename__ = 'places'

id = Column(Integer, primary_key=True)
name = Column(String, nullable=False)
description = Column(String, nullable=False)
address = Column(String, nullable=False)
latitude = Column(Float, nullable=True)
longitude = Column(Float, nullable=True)
host_id = Column(String, ForeignKey('user.id'), nullable=False)
city_id = Column(String, ForeignKey('city.id'), nullable=False)
price_per_night = Column(Integer, nullable=False)
number_of_rooms = Column(Integer, nullable=False)
number_of_bathrooms = Column(Integer, nullable=False)
max_guests = Column(Integer, nullable=False)

host = relationship("User", back_populates="places")
city = relationship("City", back_pipulates="places")

class Place(Base):
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(120), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    host_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    city_id = db.Column(db.String(36), db.ForeignKey('city.id'), nullable=False)
    price_per_night = db.Column(db.Integer, nullable=False)
    number_of_bedrooms = db.Column(db.Integer, nullable=False)
    max_guests = db.Column(db.Integer, nullable=False)

    def __init__(self, name: str, description: str, address: str, latitude: float, longitude: float, host_id: str, city_id: str, price_per_night: int, number_of_bedrooms: int, max_guests: int, **kw) -> None:
        super().__init__(**kw)
        self.name = name
        self.description = description
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.city_id = city_id
        self.price_per_night = price_per_night
        self.number_of_bedrooms = number_of_bedrooms
        self.max_guests = max_guests

    def __repr__(self) -> str:
        return f"<Place {self.name} {self.city_id} {self.host_id}>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "host_id": self.host_id,
            "city_id": self.city_id,
            "price_per_night": self.price_per_night,
            "number_of_bedrooms": self.number_of_bedrooms,
            "max_guests": self.max_guests
        }

    def create(self):
        """Create a new place"""
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        """Update an existing place"""
        db.session.commit()
        return


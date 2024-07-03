"""
Review related functionality
"""
from src import db
from src.models.base import Base
from src.models.place import Place
from src.models.user import User
from sqlalchemy import Column, String, Float, Integer, ForeignKey

__tablename__ = 'reviews'

id = Column(Integer, primary_key=True)
place_id = Column(String, ForeingKey('places.id'), nullable=False)
user_id = Column(String, ForeignKey('user.id'),nullable=False)
comment = Column(String, nullable=False)
rating = Column(Float, nullable=False)

class Review(Base):
    """Review representation"""

    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)

    def __init__(self, place_id: str, user_id: str, rating: int, comment: str = None, **kw) -> None:
        super().__init__(**kw)
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment

    def __repr__(self) -> str:
        return f"<Review {self.place_id} {self.user_id} {self.rating}>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "place_id": self.place_id,
            "user_id": self.user_id,
            "rating": self.rating,
            "comment": self.comment
        }

    def create(self):
        """Create a new review"""
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        """Update an existing review"""
        db.session.commit()
        return self
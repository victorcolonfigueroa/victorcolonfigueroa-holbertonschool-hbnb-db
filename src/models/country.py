"""
Country related functionality
"""
from src import db
from src.models.base import Base

class Country(Base):
    name = db.Column(db.String(120), nullable=False)
    code = db.Column(db.String(2), nullable=False)
    cities = db.relationship('City', backref='country', lazy=True)

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


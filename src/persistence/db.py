"""
  Now is easy to implement the database repository. The DBRepository
  should implement the Repository (Storage) interface and the methods defined
  in the abstract class Storage.

  The methods to implement are:
    - get_all
    - get
    - save
    - update
    - delete
    - reload (which can be empty)
"""

from src.models.base import Base
from src.persistence.repository import Repository
from src.models import db
from sqlalchemy.exc import SQLAlchemyError
from utils.populate import populate_db

class DBRepository(Repository):
    """Dummy DB repository"""
    def __init__(self) -> None:
        self.__session = None
        self.reload()
           
   # def __init__(self) -> None:
        """Initialize the DBRepository"""
    #    super().__init__()
        # Add any additional initialization code here

    def get_all(self, model_name: str) -> list:
        try:
            return self.__session.query(model_name).all()
        except SQLAlchemyError:
            self.__session.rollback()
        return []

    def get(self, model_name: str, obj_id: str) -> Base | None:
        try:
            return self.__session.query(model_name).get(obj_id)
        except SQLAlchemyError:
            self.__session.rollback()
            return None

    def reload(self) -> None:
        self.__session = db.session
        try:
            db.create_all()
            self.__session.commit()
            populate_db(self)
            print("commited")
        except SQLAlchemyError:
            print("ERROR")
            self.__session.rollback()
            
    def save(self, obj: Base) -> None:
        try:
            self.__session.add(obj)
            self.__session.commit()
            print("user added")
        except SQLAlchemyError:
            print("ERROR")
            self.__session.rollback()

    def update(self, obj: Base) -> Base | None:
        try:
            self.__session.commit()
        except SQLAlchemyError:
            self.__session.rollback()

    def delete(self, obj: Base) -> bool:
        try:
            self.__session.delete(obj)
            self.__session.commit()
            return True
        except SQLAlchemyError:
            self.__session.rollback()
            return False

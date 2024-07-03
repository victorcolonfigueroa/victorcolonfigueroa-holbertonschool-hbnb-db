import os
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from src.models.base import Base, engine
from src.models.review import Review
from config import get_database_url


class DataManager:
    def get_all(self):
        pass
    
    def get_by_id(self, record_id):
        pass
    
    def add(self, record):
        pass
    
    def update(self, record_id, **kwargs):
        pass
    
    def delete(self, record_id):
        pass
    
class FileDataManager(DataManager):
    def __init__(self, filepath):
        self.filepath = filepath
        
class DatabaseDataManager(DataManager):
    def __init__(self, session: Session):
        self.session = session 
        

def get_data_manager():
    database_url = get_database_url()
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    return DatabaseDataManager(session)

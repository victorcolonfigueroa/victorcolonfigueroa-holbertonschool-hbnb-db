from abc import ABC
from db import Config

class Persistence(ABC):
    @abstractmethod
    def save(self, data):
        pass
    
    @abstracmethod
    def find(self, identifire):
        pass
    
    @abstractmethod
    def delete(self, identifire):
        pass
    
class FIlePersistence(Persistence):
    def __init__(self, file_path):
        self.file_path = file_path
        
        
class DatabadePersistence(Persistence):
    def __init__(self, databese_uri):
        self.database.uri = database_uri
        

def get_persistence():
    if Config.PERSISTENCE_MODE == 'databse':
        return DatabasePersistece(Config.DATABASE_URI)
    else:
        return FIlePersistence(Config.FILE_PATH)

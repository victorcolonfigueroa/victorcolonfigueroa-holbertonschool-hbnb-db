from .persistence import Persistence

class FilePersistence(Persistence):
    def __init__(self, file_path):
        self.path = file_path
        
    def save(self, data):
        pass
    
    def find(self, identifier):
        pass
    

class DatabasePersistence(Persistence):
    def __init__(self, database_uri):
        self.database_uri = database_uri
        pass
    
    def save(self, data:):
        pass
    
    def find(self,identifier):
        pass
    
    def delete(self, identifier):
        pass

import os

class Util:
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        pass

    def get_database_path(self):
        return os.path.join(self.BASE_DIR, "database", "record.db")
    
    def get_record_path(self):
        return os.path.join(self.BASE_DIR, "record", "Record Tree.json")

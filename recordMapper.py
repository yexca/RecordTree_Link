import sqlite3
from util import Util
from datetime import datetime

class RecordMapper:
    def __init__(self):
        util = Util()
        self.conn = sqlite3.connect(util.get_database_path())
        self.cursor = self.conn.cursor()

    def file_is_existed(self, link):
        self.cursor.execute("select * from record where link = ?", (link, ))
        row = self.cursor.fetchone()

        if row is None:
            return False
        return True
    
    def add_record(self, authorId, name, date, size, link):
        addedDate = datetime.now().strftime("%Y-%m-%d")
        self.cursor.execute("""
            insert into 
            record (author_id, name, date, size, link, added_date, downloaded_date)
            values (?, ?, ?, ?, ?, ?, 0)
            """, (authorId, name, date, size, link, addedDate)
        )
        self.conn.commit()
        return True
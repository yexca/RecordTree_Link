from util import Util
import sqlite3
from datetime import datetime

class AuthorMapper:
    def __init__(self):
        util = Util()
        self.conn = sqlite3.connect(util.get_database_path())
        self.cursor = self.conn.cursor()

    def get_author_id(self, name):
        self.cursor.execute(f"select author_id from author where name = ?", (name, ))
        row = self.cursor.fetchone()

        if row is None:
            return False
        return row[0]
        
    def add_author(self, name):
        date = datetime.now().strftime("%Y-%m-%d")
        self.cursor.execute(f"insert into author (name, added_date) values (?, ?)", (name, date, ))
        self.conn.commit()
        return self.cursor.lastrowid
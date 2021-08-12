import sqlite3
from sqlite3 import Error

class MyModel:
    def __init__(self):
        pass

    def sql_connection(self):
        db_name = 'kiss.db'
        self.db_name = db_name
        
        try:
            self.con = sqlite3.connect(self.db_name)
            self.cur = self.con.cursor()
            self.cur.execute('create table if not exists mytasks (id integer PRIMARY KEY, name text, date text, type text, description text)')
            self.con.commit()
        except Error:
            return Error()
        finally:
            self.con.close()

    def tasks(self, name, desc, type, date):
        self.name = name
        self.desc = desc
        self.type = type
        self.date = date

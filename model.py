import sqlite3
from sqlite3 import Error

class MyModel:
    def __init__(self):
        pass
    
    db_name = 'kiss.db'

    def sql_connection(self):        
        try:
            con = sqlite3.connect(self.db_name)
            return con
        except Error:
            return Error()


    def sql_table(self, con):
        cur = con.cursor()
        cur.execute('create table if not exists mytasks (id integer PRIMARY KEY, name text, date text, type text, description text)')
        con.commit()

    def run_query(self, query, params = ()):
        try:
            con = self.sql_connection()
            self.sql_table(con)
            cur = con.cursor()
            result = cur.execute(query, params)
            con.commit()
            return result.fetchall()
        except Error:
            return Error()
        finally:
            con.close()

    def create_task(self, name, date, type, desc):
        self.name = name
        self.date = date
        self.type = type
        self.desc = desc
        
        parameters = (self.name, self.date, self.type, self.desc)
        try:
            query = 'INSERT INTO mytasks VALUES(NULL, ?, ?, ?, ?)'
            self.run_query(query, parameters)
        except Error:
            return Error()

    def read(self, id):
        self.id = id
        try:
            query = f'SELECT name, type, date, description FROM mytasks WHERE id = "{self.id}"'
            self.run_query(query)
        except Error:
            return Error()

    def update(self, id, new_values):
        self.id = id
        self.new_values = new_values
        try:
            query = f'UPDATE mytasks SET name = "{self.new_values[0]}", type = "{self.new_values[1]}", date = "{self.new_values[2]}", description = "{self.new_values[3]}" WHERE id = "{self.id}"'
            result = self.run_query(query)
        except Error:
            return Error()

    def delete(self, id):
        self. id = id
        try:
            query = f'DELETE from mytasks WHERE id = "{self.id}"'
            result = self.run_query(query)
        except Error:
            return Error()
    
    def get_tasks(self, day):
        try:
            query = f'SELECT name FROM mytasks WHERE date = "{day}"'
            result = self.run_query(query)
            return result
        except Error:
            return Error()
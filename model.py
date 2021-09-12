import sqlite3
from sqlite3 import Error

class MyModel:
    """
    [ENG] Class in charge of creating the database and the table, if they do not already exist, and of communicating with it to do CRUD actions.
    --------
    [ESP] Clase encargada de crear la base de datos y la tabla, en caso de que no existan previamente, y de comunicarse con la misma para realizar acciones CRUD.
    """
    def __init__(self):
        pass
    
    db_name = 'studyassistant.db'

    def sql_connection(self):
        """
        [ENG] Method to connect to the application database. 
        --------
        [ESP] Método para conectarse a la base de datos de la aplicación.
        """        
        try:
            con = sqlite3.connect(self.db_name)
            return con
        except Error:
            return Error()


    def sql_table(self, con):
        """ 
        [ENG] Method that creates a table, if it does not already exist.
        --------
        [ESP] Método que crea una tabla, si la misma no existe previamente. 
        """
        cur = con.cursor()
        cur.execute('create table if not exists mytasks (id integer PRIMARY KEY, name text, date text, type text, description text)')
        con.commit()

    def run_query(self, query, params = ()):
        """
        [ENG] Method to execute a query to the database, returning the results obtained according to the indicated query.
        --------
        [ESP] Método para ejecutar una consulta a la base de datos, retornando los resultados obtenidos segun la consulta indicada.
        """
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
        """ 
        [ENG] Method to create a new task in the database.
        --------
        [ESP] Método de creación de una nueva tarea en la base de datos.
        """
        parameters = (name, date, type, desc)
        try:
            query = 'INSERT INTO mytasks VALUES(NULL, ?, ?, ?, ?)'
            self.run_query(query, parameters)
        except Error:
            return Error()

    def read(self, id):
        """
        [ENG] Method to read the values ​​stored in a database according to a given id.
        --------
        [ESP] Método de lectura de los valores guardados en la base de datos según un id dado.
        """
        try:
            query = f'SELECT name, date, type, description FROM mytasks WHERE id = "{id}"'
            results = self.run_query(query)
            return results
        except Error:
            return Error()

    def update(self, id, nname, ndate, ntype, ndesc):
        """
        [ENG] Method to edit the values ​​stored in the database for a task according to a given id.
        --------
        [ESP] Método de edición de los valores guardados en la base de datos para una tarea en partircular según un id dado.
        """
        try:
            query = f'UPDATE mytasks SET name = "{nname}", date = "{ndate}", type = "{ntype}", description = "{ndesc}" WHERE id = "{id}"'
            result = self.run_query(query)
        except Error:
            return Error()

    def delete(self, id):
        """
        [ENG] Method that removes an entry from a database according to a given id.
        --------
        [ESP] Método que elimina una entrada de una base de datos según un id dado.
        """
        try:
            query = f'DELETE from mytasks WHERE id = "{id}"'
            result = self.run_query(query)
        except Error:
            return Error()
    
    def get_tasks(self, day):
        """
        [ENG] Method that returns all the entries in a database for a given date field value.
        --------
        [ESP] Método que retorna todas las entradas de una base de datos para un valor del campo date determinado.
        """
        try:
            query = f'SELECT id, name FROM mytasks WHERE date = "{day}"'
            result = self.run_query(query)
            return result
        except Error:
            return Error()
from datetime import datetime
from datetime import timedelta
from tkinter import messagebox
from tkinter.constants import END
from model import MyModel
from functions import format_day
from functions import get_day_name_from_strvar
from functions import input_validation

class Handler:
    """
    [ENG] Class in charge of handling the communication between the view and the model.
    --------
    [ESP] Clase encargada de manejar la comunicación entre la vista y el modelo.
    """
    def __init__(self):
        self.task_manager = MyModel()

    def handler_tasks_list(self, date, tree):
        """
        [ENG] Method that returns the list of tasks in the Treeview for a specific date.
        --------
        [ESP] Método que retorna la lista de tareas en el Treeview para una fecha determinada.
        """
        day = date.get()
        records = tree.get_children()
        for r in records:
            tree.delete(r)
        list_of_tasks = self.task_manager.get_tasks(day)
        for t in list_of_tasks:
            my_iid = t[0]
            tree.insert('', END, text = t[1], iid = my_iid)

    def handler_add(self, add_window, ninput, dainput, tinput, deinput, tree, str_value_of_day):
        """
        [ENG] Method that takes the data entered by the user to create a new task.
        --------
        [ESP] Método que toma los datos ingresados por el usuario para crear una nueva tarea.
        """
        name = ninput.get()
        date = dainput.get()
        type = tinput.get()
        desc = deinput.get(1.0, END)


        if input_validation(name, date, type) == True:
            self.task_manager.create_task(name, date, type, desc)
            add_window.destroy()
            self.handler_tasks_list(str_value_of_day, tree)
            messagebox.showinfo(message='Task successfully created')
    
    def handler_read(self, id):
        """
        [ENG] Method that takes the task selected by the user and returns the task values ​​from the database for reading.
        --------
        [ESP] Método que toma la tarea seleccionada por el usuario y devuelve los valores de la tarea desde la base de datos para su lectura.
        """
        results = self.task_manager.read(id)
        values = results[0]
        return values

    def handler_delete(self, id, tree, str_value_of_day):
        """
        [ENG] Method that removes a selected task from the database, and reloads the data in the Treeview so that it no longer appears.
        --------
        [ESP] Método que elimina una tarea seleccioanda en la base de datos, y vuelve a cargar los datos en el Treeview para que la misma no aparezca más.
        """
        self.task_manager.delete(id)
        self.handler_tasks_list(str_value_of_day, tree)
        messagebox.showinfo(message='Task successfully deleted')
    
    def handler_edit(self, id, ninput, dainput, tinput, deinput, tree, window, str_value_of_day):
        """
        [ENG] Method that takes the data entered by the user to edit a previously selected task, saving the changes in the database.
        --------
        [ESP] Método que toma los datos ingresados por el usuario para editar una tarea previamente seleccionada, guardando los cambios en la base de datos.
        """
        name = ninput.get()
        date = dainput.get()
        type = tinput.get()
        desc = deinput.get(1.0, END)

        if input_validation(name, date, type) == True:
            self.task_manager.update(id, name, date, type, desc)
            window.destroy()
            self.handler_tasks_list(str_value_of_day, tree)
            messagebox.showinfo(message='Task successfully edited')

    def handler_next_day(self, date, name_day, tree):
        """
        [ENG] Method that allows obtaining the day following the one currently displayed on the screen, changing the day's values ​​on the main screen and loading the list of tasks for that particular day.
        --------
        [ESP] Método que permite obtener el día siguiente al mostrado actualmente en pantalla, cambiando los valores del día en la pantalla principal y cargando el listado de tareas para ese día en particular.
        """
        day = date.get()
        today = datetime.strptime(day, '%d/%m/%Y')
        next_day = today + timedelta(days=1)
        date.set(format_day(next_day))
        get_day_name_from_strvar(next_day, name_day)
        self.handler_tasks_list(date, tree)

    def handler_day_before(self, date, name_day, tree):
        """
        [ENG] Method that allows obtaining the day before the one currently displayed on the screen, changing the day's values ​​on the main screen and loading the list of tasks for that particular day.
        --------
        [ESP] Método que permite obtener el día anterior al mostrado actualmente en pantalla, cambiando los valores del día en la pantalla principal y cargando el listado de tareas para ese día en particular.
        """
        day = date.get()
        today = datetime.strptime(day, '%d/%m/%Y')
        day_before = today - timedelta(days=1)
        date.set(format_day(day_before))
        get_day_name_from_strvar(day_before, name_day)
        self.handler_tasks_list(date, tree)

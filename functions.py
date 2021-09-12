from tkinter import messagebox
from datetime import datetime
import re

def get_day(name_day):
    """
    [ENG] Function that allows to retrieve the day of the date and return it in a dd/mm/yyyy format, as well as the day of the week of that date.
    --------
    [ESP] Función que permite recuperar el día de la fecha y devolver la misma en un formato de dd/mm/aaaa, asi como tambien el día de la semana de dicha fecha.
    """
    today = datetime.now()
    format = today.strftime('%d/%m/%Y')
    
    name_day.set(today.strftime('%A'))
    return format

def format_day(day):
    """
    [ENG] Function that, from a given date, returns it in a dd/mm/yyyy format.
    --------
    [ESP] Función que, a partir de una fecha dada, retorna la misma en formato dd/mm/aaaa.
    """
    format = day.strftime('%d/%m/%Y')
    return format

def get_day_name():
    """
    [ENG] Function that, from a given date, returns the name of the day of the week of that date.
    --------
    [ESP] Función que, a partir de una fecha dada, retorna el nombre del día de la semana de dicha fecha.
    """
    day = datetime.today().strftime('%A')
    return day

def get_day_name_from_strvar(next_day, name_day):
    """
    [ENG] Function that, from a given date, returns the name of the day of the week of the date and sets it in an StringVar element.
    --------
    [ESP] Función que, a partir de una fecha dada, retorna el nombre del día de la semana de dicha fecha y lo setea en un elemento de tipo StringVar.
    """
    day_name = next_day.strftime('%A')
    name_day.set(day_name)


def check_selection(tree):
    """
    [ENG] Function that checks that the user has selected a task from the list to use the buttons that require it, such as DELETE (from home) or READ.
    --------
    [ESP] Función que chequea que el usuario haya seleccionado una tarea del listado para utilizar los botones que lo requieren, como DELETE (desde el home) o READ.
    """
    try: 
        tree.item(tree.selection())['text'][0]
        return True
    except IndexError as e:
        messagebox.showinfo(message='Please select a task', title='')
        return

def get_index(type):
    """
    [ENG] Function that allows obtaining the position index of a list that is used to set the value of the task type in the read window.
    --------
    [ESP] Función que permite obtener el índice de posición de un listado que luego es utilizado para setear el valor del tipo de tarea en la ventana de lectura.
    """
    values = ['Final exam', 'Midterm exam', 'Homework', 'Reading', 'Other']
    if type == values[0]:
        return 0
    elif type == values[1]:
        return 1
    elif type == values[2]:
        return 2
    elif type == values[3]:
        return 3
    else:
        return 4

def input_validation(name, date, type):
    """
    [ENG] Function that allows validating the values ​​entered in the name field, as well as validating that the name, date and type values ​​are not empty when creating a task or editing it.
    --------
    [ESP] Función que permite validar los valores ingresados en el campo de nombre, así como validar que los valores de nombre, fecha y tipo no esten vacíos al momento de crear una tarea o editarla.
    """
    r_name = re.search(r'^[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$', name)

    if r_name == None:
        messagebox.showinfo(message="Please complete the Task's name only with valid characters", title='')
    else:
        if len(date) != 0 and len(type) != 0:
            return True
        else:
            messagebox.showinfo(message='Name, date and type are required.')

def pick_date(window, cal, date):
    """
    [ENG] Function that allows from the selection of a date in the calendar, take that value and set it in the add or edit window of the task. Also, close the calendar window to return to the add or edit window.
    --------
    [ESP] Función que permite a partir de la selección de una fecha en el calendario, tomar ese valor y setearlo en la ventana de creación o edición de la tarea. Asimismo, cierra la ventana del calendario para retornar a la ventana de creación o edición.
    """
    date.set(cal.get_date())
    window.destroy()
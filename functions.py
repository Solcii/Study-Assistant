from tkinter import messagebox
from datetime import datetime

def get_day():
    today = datetime.now()
    format = today.strftime('%d/%m/%Y')
    return format

def check_selection(tree):
    try: 
        tree.item(tree.selection())['text'][0]
        return True
    except IndexError as e:
        messagebox.showinfo(message='Please select a task', title='')
        return

def get_index(type):
    values = ['Examen final', 'Examen parcial', 'Entrega', 'Lectura', 'Otro']
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

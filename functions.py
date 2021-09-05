from tkinter import messagebox
from datetime import date, datetime
import re

def get_day(name_day):
    today = datetime.now()
    format = today.strftime('%d/%m/%Y')
    
    name_day.set(today.strftime('%A'))
    return format

def format_day(day):
    format = day.strftime('%d/%m/%Y')
    return format

def get_day_name():
    day = datetime.today().strftime('%A')
    return day

def get_day_name_from_strvar(next_day, name_day):
    day_name = next_day.strftime('%A')
    name_day.set(day_name)


def check_selection(tree):
    try: 
        tree.item(tree.selection())['text'][0]
        return True
    except IndexError as e:
        messagebox.showinfo(message='Please select a task', title='')
        return

def get_index(type):
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
    r_name = re.search(r'^[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$', name)
    if r_name != None and len(date) != 0 and len(type) != 0:
        return True

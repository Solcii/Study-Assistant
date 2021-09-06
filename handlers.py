from datetime import datetime
from datetime import timedelta
from tkinter import Label
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter.constants import END
from model import MyModel
from functions import format_day
from functions import get_day_name_from_strvar
from functions import input_validation

class Handler:
    def __init__(self):
        self.task_manager = MyModel()

    def show_header(self, window):
        self.header = PhotoImage(file='images/header_2.png').subsample(2)
        label_header = Label(window, image=self.header)
        label_header.grid(row=0, column=0, sticky='we', columnspan=3)

    def show_footer(self, window, row):        
        footer_label = Label(window, text='Made with love by Solcii')
        footer_label.config(fg='white', bg='#9463AD', font=('Verdana', 7, 'italic'), borderwidth=5)
        footer_label.grid(row=row, column=0, sticky='we', columnspan=3)

    def handler_tasks_list(self, date, tree):
        day = date.get()
        records = tree.get_children()
        for r in records:
            tree.delete(r)
        list_of_tasks = self.task_manager.get_tasks(day)
        for t in list_of_tasks:
            my_iid = t[0]
            tree.insert('', END, text = t[1], iid = my_iid)

    def handler_add(self, add_window, ninput, dainput, tinput, deinput, tree, str_value_of_day):
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
        results = self.task_manager.read(id)
        values = results[0]
        return values

    def handler_delete(self, id, tree, str_value_of_day):
        self.task_manager.delete(id)
        self.handler_tasks_list(str_value_of_day, tree)
        messagebox.showinfo(message='Task successfully deleted')
    
    def handler_edit(self, id, ninput, dainput, tinput, deinput, tree, window, str_value_of_day):
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
        day = date.get()
        today = datetime.strptime(day, '%d/%m/%Y')
        next_day = today + timedelta(days=1)
        date.set(format_day(next_day))
        get_day_name_from_strvar(next_day, name_day)
        self.handler_tasks_list(date, tree)

    def handler_day_before(self, date, name_day, tree):
        day = date.get()
        today = datetime.strptime(day, '%d/%m/%Y')
        day_before = today - timedelta(days=1)
        date.set(format_day(day_before))
        get_day_name_from_strvar(day_before, name_day)
        self.handler_tasks_list(date, tree)







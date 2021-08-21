from tkinter import Label
from tkinter import messagebox
from tkinter.constants import END
from model import MyModel
from functions import get_day

class Handler:
    def __init__(self):
        self.task_manager = MyModel()

    def show_header(self, window):
        title_label = Label(window, text='Keep it simple, studying')
        title_label.config(fg='white', bg='lightblue', font='Verdana, 15')
        title_label.grid(row=0, column=0, sticky='we', columnspan=3)

    def show_footer(self, window, row):
        footer_label = Label(window, text='Made with love')
        footer_label.config(fg='white', bg='darkblue', font='Verdana, 6')
        footer_label.grid(row=row, column=0, sticky='we', columnspan=3)

    def handler_tasks_list(self, tree):
        day = get_day()
        records = tree.get_children()
        for r in records:
            tree.delete(r)
        list_of_tasks = self.task_manager.get_tasks(day)
        for t in list_of_tasks:
            my_iid = t[0]
            tree.insert('', END, text = t[1], iid = my_iid)

    def handler_add(self, add_window, ninput, dainput, tinput, deinput, tree):
        name = ninput.get()
        date = dainput.get()
        type = tinput.get()
        desc = deinput.get(1.0, END)

        self.task_manager.create_task(name, date, type, desc)
        add_window.destroy()
        self.handler_tasks_list(tree)
        messagebox.showinfo(message='Task successfully created')
    
    def handler_read(self, id):
        results = self.task_manager.read(id)
        values = results[0]
        return values

    def handler_delete(self, id, tree):
        self.task_manager.delete(id)
        self.handler_tasks_list(tree)
        messagebox.showinfo(message='Task successfully deleted')
    
    def handler_edit(self, id, ninput, dainput, tinput, deinput, tree, window):
        name = ninput.get()
        date = dainput.get()
        type = tinput.get()
        desc = deinput.get(1.0, END)
        self.task_manager.update(id, name, date, type, desc)
        window.destroy()
        self.handler_tasks_list(tree)
        messagebox.showinfo(message='Task successfully edited')





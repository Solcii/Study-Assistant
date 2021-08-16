from calendar import month
from tkinter import Tk
from tkinter import StringVar
from tkinter import Toplevel
from tkinter import Label
from tkinter import Button
from tkinter import Frame
from tkinter import Entry
from tkinter import Text
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime
from tkinter.constants import CENTER, END
from tkinter.constants import DISABLED
from model import MyModel
from handlers import get_day


class MyView:
    def __init__(self, window):
        self.task = MyModel()
        self.window = window
        self.window.title('K.I.S.S.')
        Tk.iconbitmap(self.window, default='kicon.ico')
        self.window.config(background='#fafafa')

        #PRINCIPAL VIEW
        #Header
        title_label = Label(self.window, text='Keep it simple, studying')
        title_label.config(fg='white', bg='lightblue', font='Verdana, 15')
        title_label.grid(row=0, column=0, sticky='we', columnspan=3)

        #Date view
        yesterday_button = Button(self.window, text = '🡰',command = lambda: print('Hola'))
        yesterday_button.grid(row=1, column=0, rowspan=2)

        tomorrow_button = Button(self.window, text='🡲',command = lambda: print('Hola'))
        tomorrow_button.grid(row=1, column=2, rowspan=2)
        
        day_label = Label(self.window, text='HOY')
        day_label.config(fg='blue', bg='#fafafa', font='Verdana, 8')
        day_label.grid(row=1, column=1)
        
        self.day = get_day()
        
        data_label = Label(self.window, text=self.day)
        data_label.config(fg='blue', bg='#fafafa', font='Verdana, 8')
        data_label.grid(row=2, column=1)

        #List tasks

        frame = Frame(self.window)
        frame.grid(row=3, column=0, columnspan=3)

        list_of_tasks = ttk.Treeview(frame, selectmode='browse', height=10)
        list_of_tasks.heading('#0', text='Tareas', anchor=CENTER)
        list_of_tasks.grid(row=3, column=0, columnspan=3)

        sb = ttk.Scrollbar(frame, orient='vertical', command=list_of_tasks.yview)
        sb.grid(row=3, column=4, sticky='nse')


        #Buttons

        add_button = Button(text='ADD', command=self.open_add_view)
        add_button.grid(row=4, column=0, sticky='we')

        read_button = Button(text='READ')
        read_button.grid(row=4, column=1, sticky='we')

        delete_button = Button(text='DELETE')
        delete_button.grid(row=4, column=2, sticky='we')

        #Footer
        footer_label = Label(self.window, text='Made with love')
        footer_label.config(fg='white', bg='darkblue', font='Verdana, 6')
        footer_label.grid(row=5, column=0, sticky='we', columnspan=3)

        #Handler Functions
    def handler_create_task(self):
        pass



    #ADD VIEW
    def open_add_view(self):
        self.add_window = Toplevel()
        self.add_window.title('Add task')

        #Header
        title_label = Label(self.add_window, text='Keep it simple, studying')
        title_label.config(fg='white', bg='lightblue', font='Verdana, 15')
        title_label.grid(row=0, column=0, sticky='we', columnspan=3)

        #Inputs
        task_name_label = Label(self.add_window, text='Titulo: ')
        task_name_label.grid(row=1, column=0)
        self.task_name_input = Entry(self.add_window)
        self.task_name_input.grid(row=1, column=1, columnspan=2)

        self.date_selected = StringVar()

        task_date_label = Label(self.add_window, text='Fecha: ')
        task_date_label.grid(row=2, column=0)
        self.task_date_input = Entry(self.add_window, state=DISABLED, textvariable=self.date_selected)
        self.task_date_input.grid(row=2, column=1)
        self.task_date_button = Button(self.add_window, text='Select date', command=self.open_calendar)
        self.task_date_button.grid(row=2, column=2)

        task_type_label = Label(self.add_window, text='Tipo: ')
        task_type_label.grid(row=3, column=0)
        self.task_type_input = ttk.Combobox(self.add_window, state='readonly')
        self.task_type_input['values'] = ['Examen final', 'Examen parcial', 'Entrega', 'Lectura', 'Otro']
        self.task_type_input.grid(row=3, column=1, columnspan=2)

        task_desc_label = Label(self.add_window, text='Descripcion: ')
        task_desc_label.grid(row=4, column=0)
        self.task_desc_input = Text(self.add_window, width=30, height=5)
        self.task_desc_input.grid(row=5, column=0, columnspan=3)

        #Button
        save_button = Button(self.add_window, text='SAVE', command=self.handler_add)
        save_button.grid(row=6, column=0, sticky='we', columnspan=3)

        #Footer
        footer_label = Label(self.add_window, text='Made with love')
        footer_label.config(fg='white', bg='darkblue', font='Verdana, 6')
        footer_label.grid(row=7, column=0, sticky='we', columnspan=3)

    def open_calendar(self):
        self.calendar_window = Toplevel()
        self.calendar_window.title('Select a date')

        year = datetime.today().year
        month = datetime.today().month
        day = datetime.today().day
        
        
        self.cal = Calendar(self.calendar_window, selectmode='day', year=year, month=month, day=day)
        self.cal.grid(row=0, column=0)

        get_date_button = Button(self.calendar_window, text='Seleccionar', command=self.pick_date)
        get_date_button.grid(row=1, column=0)

    def pick_date(self):
        self.date_selected.set(self.cal.get_date())
        self.calendar_window.destroy()
    
    def handler_add(self):
        self.name = self.task_name_input.get()
        self.date = self.task_date_input.get()
        self.type = self.task_type_input.get()
        self.desc = self.task_desc_input.get(1.0, END)

        self.task.create_task(self.name, self.date, self.type, self.desc)
        self.add_window.destroy()















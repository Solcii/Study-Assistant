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
from tkinter.constants import CENTER
from tkinter.constants import END
from tkinter.constants import DISABLED
from handlers import VisualHandler
from functions import get_day


class MyView:
    def __init__(self, window):
        self.visual_handler = VisualHandler()
        self.window = window
        self.window.title('K.I.S.S.')
        Tk.iconbitmap(self.window, default='kicon.ico')
        self.window.config(background='#fafafa')

        #PRINCIPAL VIEW
        #Header
        self.visual_handler.show_header(self.window)

        #Date view
        yesterday_button = Button(self.window, text = '🡰',command = lambda: print('Hola'))
        yesterday_button.grid(row=1, column=0, rowspan=2)

        tomorrow_button = Button(self.window, text='🡲',command = lambda: print('Hola'))
        tomorrow_button.grid(row=1, column=2, rowspan=2)
        
        day_label = Label(self.window, text='HOY')
        day_label.config(fg='blue', bg='#fafafa', font='Verdana, 8')
        day_label.grid(row=1, column=1)
        
        day = get_day()
        
        data_label = Label(self.window, text=day)
        data_label.config(fg='blue', bg='#fafafa', font='Verdana, 8')
        data_label.grid(row=2, column=1)

        #List tasks

        frame = Frame(self.window)
        frame.grid(row=3, column=0, columnspan=3)

        self.list_of_tasks = ttk.Treeview(frame, selectmode='browse', height=10)
        self.list_of_tasks.heading('#0', text='Tareas', anchor=CENTER)
        self.list_of_tasks.grid(row=3, column=0, columnspan=3)

        sb = ttk.Scrollbar(frame, orient='vertical', command=self.list_of_tasks.yview)
        sb.grid(row=3, column=4, sticky='nse')

        self.visual_handler.handler_tasks_list(self.list_of_tasks)


        #Buttons

        add_button = Button(text='ADD', command=self.open_add_view)
        add_button.grid(row=4, column=0, sticky='we')

        read_button = Button(text='READ', command=self.open_read_view)
        read_button.grid(row=4, column=1, sticky='we')

        delete_button = Button(text='DELETE')
        delete_button.grid(row=4, column=2, sticky='we')

        #Footer
        self.visual_handler.show_footer(self.window, 5)

    #ADD VIEW
    def open_add_view(self):
        add_window = Toplevel()
        add_window.title('Add task')

        #Header
        self.visual_handler.show_header(add_window)

        #Inputs
        task_name_label = Label(add_window, text='Titulo: ')
        task_name_label.grid(row=1, column=0)
        task_name_input = Entry(add_window)
        task_name_input.grid(row=1, column=1, columnspan=2)

        self.date_selected = StringVar()

        task_date_label = Label(add_window, text='Fecha: ')
        task_date_label.grid(row=2, column=0)
        task_date_input = Entry(add_window, state=DISABLED, textvariable=self.date_selected)
        task_date_input.grid(row=2, column=1)
        task_date_button = Button(add_window, text='Select date', command=self.open_calendar)
        task_date_button.grid(row=2, column=2)

        task_type_label = Label(add_window, text='Tipo: ')
        task_type_label.grid(row=3, column=0)
        task_type_input = ttk.Combobox(add_window, state='readonly')
        task_type_input['values'] = ['Examen final', 'Examen parcial', 'Entrega', 'Lectura', 'Otro']
        task_type_input.grid(row=3, column=1, columnspan=2)

        task_desc_label = Label(add_window, text='Descripcion: ')
        task_desc_label.grid(row=4, column=0)
        task_desc_input = Text(add_window, width=30, height=5)
        task_desc_input.grid(row=5, column=0, columnspan=3)

        #Button
        save_button = Button(add_window, text='SAVE', command=lambda: self.visual_handler.handler_add(add_window, task_name_input, task_date_input, task_type_input, task_desc_input, self.list_of_tasks))
        save_button.grid(row=6, column=0, sticky='we', columnspan=3)

        #Footer
        self.visual_handler.show_footer(add_window, 7)

    
    #READ VIEW
    def open_read_view(self):
        read_window = Toplevel()
        read_window.title('Your task')

        #Header
        self.visual_handler.show_header(read_window)

        #Inputs
        task_name_label = Label(read_window, text='Titulo: ')
        task_name_label.grid(row=1, column=0)
        self.task_name_input = Entry(read_window, state=DISABLED)
        self.task_name_input.grid(row=1, column=1, columnspan=2)

        self.date_selected = StringVar()

        task_date_label = Label(read_window, text='Fecha: ')
        task_date_label.grid(row=2, column=0)
        self.task_date_input = Entry(read_window, state=DISABLED, textvariable=self.date_selected)
        self.task_date_input.grid(row=2, column=1)
        self.task_date_button = Button(read_window, text='Select date', command=self.open_calendar, state=DISABLED)
        self.task_date_button.grid(row=2, column=2)

        task_type_label = Label(read_window, text='Tipo: ')
        task_type_label.grid(row=3, column=0)
        self.task_type_input = ttk.Combobox(read_window, state='readonly')
        self.task_type_input['values'] = ['Examen final', 'Examen parcial', 'Entrega', 'Lectura', 'Otro']
        self.task_type_input.grid(row=3, column=1, columnspan=2)

        task_desc_label = Label(read_window, text='Descripcion: ')
        task_desc_label.grid(row=4, column=0)
        self.task_desc_input = Text(read_window, width=30, height=5, state=DISABLED)
        self.task_desc_input.grid(row=5, column=0, columnspan=3)

        #Button
        home_button = Button(read_window, text='HOME')
        home_button.grid(row=6, column=0, sticky='we')

        edit_button = Button(read_window, text='EDIT')
        edit_button.grid(row=6, column=1, sticky='we')

        delete_button = Button(read_window, text='DELETE')
        delete_button.grid(row=6, column=2, sticky='we')

        #Footer
        self.visual_handler.show_footer(read_window, 7)

    
    
    #HANDLER FUNCTIONS
    def open_calendar(self):
        calendar_window = Toplevel()
        calendar_window.title('Select a date')

        year = datetime.today().year
        month = datetime.today().month
        day = datetime.today().day
        
        
        self.cal = Calendar(calendar_window, selectmode='day',date_pattern='dd/mm/y' ,year=year, month=month, day=day)
        self.cal.grid(row=0, column=0)

        get_date_button = Button(calendar_window, text='Seleccionar', command= lambda: self.pick_date(calendar_window))
        get_date_button.grid(row=1, column=0)

    def pick_date(self, window):
        self.date_selected.set(self.cal.get_date())
        self.window.destroy()

    














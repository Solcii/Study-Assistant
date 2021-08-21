from tkinter import Tk
from tkinter import StringVar
from tkinter import Toplevel
from tkinter import Label
from tkinter import Button
from tkinter import Frame
from tkinter import Entry
from tkinter import Text
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
from tkinter.constants import CENTER
from tkinter.constants import END
from tkinter.constants import DISABLED
from tkinter.constants import NORMAL
from handlers import Handler
from functions import get_day
from functions import check_selection
from functions import get_index


class MyView:
    def __init__(self, window):
        self.handler = Handler()
        self.window = window
        self.window.title('K.I.S.S.')
        Tk.iconbitmap(self.window, default='kicon.ico')
        self.window.config(background='#fafafa')

        #PRINCIPAL VIEW
        #Header
        self.handler.show_header(self.window)

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

        self.handler.handler_tasks_list(self.list_of_tasks)


        #Buttons

        add_button = Button(text='ADD', command=lambda: self.open_add_view(self.list_of_tasks))
        add_button.grid(row=4, column=0, sticky='we')

        read_button = Button(text='READ', command=lambda: self.open_read_view(self.list_of_tasks))
        read_button.grid(row=4, column=1, sticky='we')

        delete_button = Button(text='DELETE', command=lambda: self.delete_from_home(self.list_of_tasks))
        delete_button.grid(row=4, column=2, sticky='we')

        #Footer
        self.handler.show_footer(self.window, 5)

    #ADD VIEW
    def open_add_view(self, tree):
        add_window = Toplevel()
        add_window.title('Add task')

        #Header
        self.handler.show_header(add_window)

        #Inputs
        task_name_label = Label(add_window, text='Titulo: ')
        task_name_label.grid(row=1, column=0)
        task_name_input = Entry(add_window)
        task_name_input.grid(row=1, column=1, columnspan=2)

        date_selected = StringVar()

        task_date_label = Label(add_window, text='Fecha: ')
        task_date_label.grid(row=2, column=0)
        task_date_input = Entry(add_window, state=DISABLED, textvariable=date_selected)
        task_date_input.grid(row=2, column=1)
        task_date_button = Button(add_window, text='Select date', command= lambda: self.open_calendar(date_selected))
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
        save_button = Button(add_window, text='SAVE', command=lambda: self.handler.handler_add(add_window, task_name_input, task_date_input, task_type_input, task_desc_input, tree))
        save_button.grid(row=6, column=0, sticky='we', columnspan=3)

        #Footer
        self.handler.show_footer(add_window, 7)

    
    #READ VIEW
    def open_read_view(self, tree):
        if check_selection(tree) == True:
            id = tree.selection()[0]
            values = self.handler.handler_read(id)
            name = values[0]
            date = values[1]
            type = values[2]
            desc = values[3]
            read_window = Toplevel()
            read_window.title('Your task')

            #Header
            self.handler.show_header(read_window)

            #Inputs
            task_name_label = Label(read_window, text='Titulo: ')
            task_name_label.grid(row=1, column=0)
            task_name_input = Entry(read_window, textvariable = StringVar(read_window, value=name) , state=DISABLED)
            task_name_input.grid(row=1, column=1, columnspan=2)

            task_date_label = Label(read_window, text='Fecha: ')
            task_date_label.grid(row=2, column=0)
            task_date_input = Entry(read_window, textvariable = StringVar(read_window, value=date), state=DISABLED)
            task_date_input.grid(row=2, column=1, columnspan=2)

            task_type_label = Label(read_window, text='Tipo: ')
            task_type_label.grid(row=3, column=0)
            task_type_input = Entry(read_window, textvariable = StringVar(read_window, value=type) , state=DISABLED)
            task_type_input.grid(row=3, column=1, columnspan=2)

            task_desc_label = Label(read_window, text='Descripcion: ')
            task_desc_label.grid(row=4, column=0)
            task_desc_input = Text(read_window, width=30, height=5)
            task_desc_input.insert(END, desc)
            task_desc_input.config(state=DISABLED)
            task_desc_input.grid(row=5, column=0, columnspan=3)

            #Button
            home_button = Button(read_window, text='HOME', command=lambda: read_window.destroy())
            home_button.grid(row=6, column=0, sticky='we')

            edit_button = Button(read_window, text='EDIT', command=lambda: self.open_edit_window(read_window, tree))
            edit_button.grid(row=6, column=1, sticky='we')

            delete_button = Button(read_window, text='DELETE', command=lambda: self.delete_from_read(tree, read_window))
            delete_button.grid(row=6, column=2, sticky='we')

            #Footer
            self.handler.show_footer(read_window, 7)

    
    #CALENDAR FUNCTIONS
    def open_calendar(self, date):
        calendar_window = Toplevel()
        calendar_window.title('Select a date')

        year = datetime.today().year
        month = datetime.today().month
        day = datetime.today().day
        
        cal = Calendar(calendar_window, selectmode='day',date_pattern='dd/mm/y' ,year=year, month=month, day=day)
        cal.grid(row=0, column=0)

        get_date_button = Button(calendar_window, text='Seleccionar', command= lambda: self.pick_date(calendar_window, cal, date))
        get_date_button.grid(row=1, column=0)

    def pick_date(self, window, cal, date):
        date.set(cal.get_date())
        window.destroy()

    def delete_from_home(self, tree):
        if check_selection(tree) == True:
            conf = messagebox.askyesno(message='Task will be deleted. Are you sure?', title='Delete task')

            if conf == True:
                id = tree.selection()[0]
                self.handler.handler_delete(id, tree)
    
    def delete_from_read(self, tree, window):
        conf = messagebox.askyesno(message='Task will be deleted. Are you sure?', title='Delete task')

        if conf == True:
            id = tree.selection()[0]
            self.handler.handler_delete(id, tree)
            window.destroy()

    
    #EDIT OPTION
    def open_edit_window(self, window, tree):
        window.destroy()
        edit_window = Toplevel()
        edit_window.title('Edit task')

        id = tree.selection()[0]
        values = self.handler.handler_read(id)
        name = values[0]
        date = values[1]
        type = values[2]
        desc = values[3]

        #Header
        self.handler.show_header(edit_window)

        #Inputs
        task_name_label = Label(edit_window, text='Titulo: ')
        task_name_label.grid(row=1, column=0)
        task_name_input = Entry(edit_window, textvariable = StringVar(edit_window, value=name))
        task_name_input.grid(row=1, column=1, columnspan=2)

        date_selected = StringVar(value=date)

        task_date_label = Label(edit_window, text='Fecha: ')
        task_date_label.grid(row=2, column=0)
        task_date_input = Entry(edit_window, state=DISABLED, textvariable = date_selected)
        task_date_input.grid(row=2, column=1)
        task_date_button = Button(edit_window, text='Select date', command= lambda: self.open_calendar(date_selected))
        task_date_button.grid(row=2, column=2)


        task_type_label = Label(edit_window, text='Tipo: ')
        task_type_label.grid(row=3, column=0)
        task_type_input = ttk.Combobox(edit_window, state='readonly')
        task_type_input['values'] = ['Examen final', 'Examen parcial', 'Entrega', 'Lectura', 'Otro']
        index_type = get_index(type)
        task_type_input.current(index_type)


        #task_type_input = Entry(edit_window, textvariable = StringVar(edit_window, value=type))
        task_type_input.grid(row=3, column=1, columnspan=2)

        task_desc_label = Label(edit_window, text='Descripcion: ')
        task_desc_label.grid(row=4, column=0)
        task_desc_input = Text(edit_window, width=30, height=5)
        task_desc_input.insert(END, desc)
        task_desc_input.grid(row=5, column=0, columnspan=3)    

        #Button
        save_button = Button(edit_window, text='SAVE', command=lambda: self.handler.handler_edit(id, task_name_input, task_date_input, task_type_input, task_desc_input, tree, edit_window))
        save_button.grid(row=6, column=0, sticky='we', columnspan=3)

        #Footer
        self.handler.show_footer(edit_window, 7)



    














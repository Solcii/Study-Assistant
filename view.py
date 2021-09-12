from tkinter import Tk
from tkinter import PhotoImage
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
from handlers import Handler
from functions import get_day
from functions import check_selection
from functions import get_index
from functions import pick_date


class MyView:
    """
    [ENG] Class in charge of showing all the visual elements of the application.
    --------
    [ESP] Clase encargada de mostrar todos los elementos visuales de la aplicación.
    """
    def __init__(self, window):
        """
        [ENG] Method that allows the application's main screen to be displayed when the application is initialized, taking the current day as the default date and showing the daily tasks in the list.
        --------
        [ESP] Método que permite que al inicializar la aplicación se muestre la pantalla principal de la misma, tomando como fecha por defecto el día actual y mostrando en el listado las tareas del día.
        """
        self.handler = Handler()
        self.window = window
        self.window.title('Study Assistant')
        Tk.iconbitmap(self.window, default='images/star.ico')
        self.window.config(background='#FDEFFD')

        #PRINCIPAL VIEW
        #Header
        self.header = PhotoImage(file='images/header_2.png').subsample(2)
        label_header = Label(window, image=self.header)
        label_header.grid(row=0, column=0, sticky='we', columnspan=3)

        #Date view
        self.arrow_left = PhotoImage(file='images/left.png')
        self.arrow_right = PhotoImage(file='images/right.png')


        yesterday_button = Button(self.window, image=self.arrow_left , border=0, background='#FDEFFD',command = lambda: self.handler.handler_day_before(day, day_name, self.list_of_tasks))
        yesterday_button.grid(row=1, column=0, rowspan=2)

        tomorrow_button = Button(self.window, image=self.arrow_right, border=0, background='#FDEFFD',command = lambda: self.handler.handler_next_day(day, day_name, self.list_of_tasks))
        tomorrow_button.grid(row=1, column=2, rowspan=2)

        day_name = StringVar()

        day_label = Label(self.window, textvariable=day_name)
        day_label.config(fg='#51141E', bg='#FDEFFD', font= ('Verdana', 14, 'bold'), width=10)
        day_label.grid(row=1, column=1)
        

        day = StringVar(value=get_day(day_name))
        data_label = Label(self.window, textvariable=day)
        data_label.config(fg='#51141E', bg='#FDEFFD', font=('Verdana', 9, 'italic'))
        data_label.grid(row=2, column=1)



        #List tasks

        frame = Frame(self.window)
        frame.config(background="#FDEFFD", borderwidth=5)
        frame.grid(row=3, column=0, columnspan=3)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Verdana', 10))

        style2 = ttk.Style()
        style2.configure("Treeview", font=('Verdana', 8))


        self.list_of_tasks = ttk.Treeview(frame, selectmode='browse', height=10)
        self.list_of_tasks.heading('#0', text='Tasks', anchor=CENTER)
        self.list_of_tasks.grid(row=3, column=0)

        sb = ttk.Scrollbar(frame, orient='vertical', command=self.list_of_tasks.yview)
        sb.grid(row=3, column=4, sticky='nse')

        self.handler.handler_tasks_list(day, self.list_of_tasks)


        #Buttons
        add_button = Button(text='ADD', background='#198754', foreground='#fff', activebackground='#127C4B', font=('Verdana', 9), border=2, cursor = 'hand2', command=lambda: self.open_add_view(self.list_of_tasks, day))
        add_button.config(width=10)
        add_button.grid(row=4, column=0, sticky='we')

        read_button = Button(text='READ', background= '#0d6efd', foreground='#fff', activebackground='#064095', font=('Verdana', 9), border=2, cursor = 'hand2', command=lambda: self.open_read_view(self.list_of_tasks, day))
        read_button.config(width=10)
        read_button.grid(row=4, column=1, sticky='we')

        delete_button = Button(text='DELETE', background='#dc3545', foreground='#fff', activebackground='#AF212F', font=('Verdana', 9), border=2, cursor = 'hand2',  command=lambda: self.delete_from_home(self.list_of_tasks, day))
        delete_button.config(width=10)
        delete_button.grid(row=4, column=2, sticky='we')

        #Footer
        self.show_footer(self.window, 5)

    #ADD VIEW
    def open_add_view(self, tree, str_value_of_day):
        """
        [ENG] Method that when pressing the ADD button, opens the screen to add a new task, leaving the main screen in the background.
        --------
        [ESP] Método que, al presionar el boton ADD, abre la pantalla de carga de datos, dejando la pantalla principal en segundo plano.
        """
        add_window = Toplevel()
        add_window.config(background='#FDEFFD')
        add_window.title('Add task')

        #Header
        self.show_header(add_window)

        #Inputs
        task_name_label = Label(add_window, text='Title: ')
        task_name_label.config(fg='#51141E', bg='#FDEFFD', font= ('Verdana', 10, 'bold'))
        task_name_label.configure(pady=3)
        task_name_label.grid(row=1, column=0)
        task_name_input = Entry(add_window)
        task_name_input.config(font= ('Verdana', 10, 'italic'))
        task_name_input.grid(row=1, column=1, columnspan=2)

        date_selected = StringVar()

        task_date_label = Label(add_window, text='Date: ')
        task_date_label.config(fg='#51141E', bg='#FDEFFD', font= ('Verdana', 10, 'bold'))
        task_date_label.configure(pady=3)
        task_date_label.grid(row=2, column=0)
        task_date_input = Entry(add_window, state=DISABLED, textvariable=date_selected)
        task_date_input.config(font= ('Verdana', 10, 'italic'))
        task_date_input.grid(row=2, column=1)

        self.calendar = PhotoImage(file='images/calendar.png').subsample(2)

        task_date_button = Button(add_window, image=self.calendar, background='#FDEFFD', border=0, cursor = 'hand2', command= lambda: self.open_calendar(date_selected))
        task_date_button.grid(row=2, column=2)

        task_type_label = Label(add_window, text='Type: ')
        task_type_label.config(fg='#51141E', bg='#FDEFFD', font= ('Verdana', 10, 'bold'))
        task_type_label.configure(pady=3)
        task_type_label.grid(row=3, column=0)
        task_type_input = ttk.Combobox(add_window, state='readonly')
        task_type_input['values'] = ['Final exam', 'Midterm exam', 'Homework', 'Reading', 'Other']
        task_type_input.config(font= ('Verdana', 10, 'italic'))
        task_type_input.grid(row=3, column=1, columnspan=2)

        task_desc_label = Label(add_window, text='Description: ')
        task_desc_label.config(fg='#51141E', bg='#FDEFFD', font= ('Verdana', 10, 'bold'))
        task_desc_label.configure(pady=3)
        task_desc_label.grid(row=4, column=0)
        task_desc_input = Text(add_window, width=30, height=5)
        task_desc_input.config(font= ('Verdana', 10, 'italic'), borderwidth=3, relief='groove')
        task_desc_input.grid(row=5, column=0, columnspan=3)

        #Button
        save_button = Button(add_window, text='SAVE', background='#198754', foreground='#fff', activebackground='#127C4B', font=('Verdana', 9), border=2, cursor = 'hand2', width=10, command=lambda: self.handler.handler_add(add_window, task_name_input, task_date_input, task_type_input, task_desc_input, tree, str_value_of_day))
        save_button.grid(row=6, column=0, sticky='we', columnspan=3)

        #Footer
        self.show_footer(add_window, 7)

    
    #READ VIEW
    def open_read_view(self, tree, str_value_of_day):
        """
        [ENG] Method that, when pressing the READ button, opens the data reading screen of the selected task, leaving the main screen in the background. If a task was not previously selected, it returns an error message indicating to the user that to use this button they must first select a task from the list.
        --------
        [ESP] Método que, al presionar el boton READ, abre la pantalla de lectura de datos de la tarea seleccionada, dejando la pantalla principal en segundo plano. Si no se seleccionó previamente una tarea, devuelve un mensaje de error indicando al usuario que para utilizar dicho boton primero debe seleccionar una tarea de la lista.
        """
        if check_selection(tree) == True:
            id = tree.selection()[0]
            values = self.handler.handler_read(id)
            name = values[0]
            date = values[1]
            type = values[2]
            desc = values[3]
            read_window = Toplevel()
            read_window.config(background='#FDEFFD')
            read_window.title('Your task')

            #Header
            self.show_header(read_window)

            #Inputs
            task_name_label = Label(read_window, text='Title: ')
            task_name_label.config(fg='#51141E', bg='#FDEFFD', font= ('Verdana', 10, 'bold'))
            task_name_label.configure(pady=3)
            task_name_label.grid(row=1, column=0)
            task_name_input = Entry(read_window, textvariable = StringVar(read_window, value=name) , state=DISABLED)
            task_name_input.config(font= ('Verdana', 10, 'italic'))
            task_name_input.grid(row=1, column=1, columnspan=2)

            task_date_label = Label(read_window, text='Date: ')
            task_date_label.config(fg='#51141E', bg='#FDEFFD', font= ('Verdana', 10, 'bold'))
            task_date_label.configure(pady=3)
            task_date_label.grid(row=2, column=0)
            task_date_input = Entry(read_window, textvariable = StringVar(read_window, value=date), state=DISABLED)
            task_date_input.config(font= ('Verdana', 10, 'italic'))
            task_date_input.grid(row=2, column=1, columnspan=2)

            task_type_label = Label(read_window, text='Type: ')
            task_type_label.config(fg='#51141E', bg='#FDEFFD', font= ('Verdana', 10, 'bold'))
            task_type_label.configure(pady=3)
            task_type_label.grid(row=3, column=0)
            task_type_input = Entry(read_window, textvariable = StringVar(read_window, value=type) , state=DISABLED)
            task_type_input.config(font= ('Verdana', 10, 'italic'))
            task_type_input.grid(row=3, column=1, columnspan=2)

            task_desc_label = Label(read_window, text='Description: ')
            task_desc_label.config(fg='#51141E', bg='#FDEFFD', font= ('Verdana', 10, 'bold'))
            task_desc_label.configure(pady=3)
            task_desc_label.grid(row=4, column=0)
            task_desc_input = Text(read_window, width=30, height=5)
            task_desc_input.config(font= ('Verdana', 10, 'italic'), borderwidth=3, relief='groove')
            task_desc_input.insert(END, desc)
            task_desc_input.config(state=DISABLED)
            task_desc_input.grid(row=5, column=0, columnspan=3)

            #Button
            home_button = Button(read_window, text='HOME', background='#adb5bd', foreground='#fff', activebackground='#979FA7', font=('Verdana', 9), border=2, cursor = 'hand2', width=10, command=lambda: read_window.destroy())
            home_button.grid(row=6, column=0, sticky='we')

            edit_button = Button(read_window, text='EDIT',  background= '#0d6efd', foreground='#fff', activebackground='#064095', font=('Verdana', 9), border=2, cursor = 'hand2', width=10,  command=lambda: self.open_edit_window(read_window, tree, str_value_of_day))
            edit_button.grid(row=6, column=1, sticky='we')

            delete_button = Button(read_window, text='DELETE', background='#dc3545', foreground='#fff', activebackground='#AF212F', font=('Verdana', 9), border=2, cursor = 'hand2', width=10, command=lambda: self.delete_from_read(tree, read_window, str_value_of_day))
            delete_button.grid(row=6, column=2, sticky='we')

            #Footer
            self.show_footer(read_window, 7)

    
    #CALENDAR FUNCTIONS
    def open_calendar(self, date):
        """
        [ENG] Method that allows the user to select a date for the creation or edition of a task, from the opening of a window with a calendar.
        --------
        [ESP] Método que permite al usuario seleccionar una fecha para la creación o edición de una tarea, a partir de la apertura de una ventana con un calendario.
        """
        calendar_window = Toplevel()
        calendar_window.config(background='#FDEFFD')
        calendar_window.title('Select a date')

        year = datetime.today().year
        month = datetime.today().month
        day = datetime.today().day

        calendar_frame = Frame(calendar_window)
        calendar_frame.config(background="#FDEFFD", borderwidth=5)
        calendar_frame.grid(row=0, column=0)
        
        cal = Calendar(calendar_frame, selectmode='day',date_pattern='dd/mm/y' ,year=year, month=month, day=day)
        cal.grid(row=0, column=0)

        get_date_button = Button(calendar_window, text='Select', font=('Verdana', 9), background='#0d6efd', foreground='#fff', activebackground='#064095', border=2, cursor='hand2' ,command= lambda: pick_date(calendar_window, cal, date))
        get_date_button.grid(row=1, column=0, sticky='we')

        footer = Label(calendar_window, background='#FDEFFD', font='Verdana, 1')
        footer.grid(row=2, column=0)

    def delete_from_home(self, tree, str_value_of_day):
        """
        [ENG] Method that allows the user to delete a task from the main window using the DELETE button, showing a confirmation message before proceeding to delete the task. If a task was not previously selected, it returns an error message indicating to the user that to use the button they must first select a task from the list.
        --------
        [ESP] Método que permite al usuario eliminar una tarea desde la ventana principal utilizando el boton DELETE, mostrando un mensaje de confirmación antes de proceder a eliminar dicha tarea. Si no se seleccionó previamente una tarea, devuelve un mensaje de error indicando al usuario que para utilizar el boton primero debe seleccionar una tarea de la lista.
        """
        if check_selection(tree) == True:
            conf = messagebox.askyesno(message='Task will be deleted. Are you sure?', title='Delete task')

            if conf == True:
                id = tree.selection()[0]
                self.handler.handler_delete(id, tree, str_value_of_day)
    
    def delete_from_read(self, tree, window, str_value_of_day):
        """
        [ENG] Method that allows the user to delete a task from the read window using the DELETE button, showing a confirmation message before proceeding to delete said task. If a task was not previously selected, it returns an error message indicating to the user that to use the button they must first select a task from the list.
        --------
        [ESP] Método que permite al usuario eliminar una tarea desde la ventana de lectura utilizando el boton DELETE, mostrando un mensaje de confirmación antes de proceder a eliminar dicha tarea. Si no se seleccionó previamente una tarea, devuelve un mensaje de error indicando al usuario que para utilizar el boton primero debe seleccionar una tarea de la lista.
        """
        conf = messagebox.askyesno(message='Task will be deleted. Are you sure?', title='Delete task')

        if conf == True:
            id = tree.selection()[0]
            self.handler.handler_delete(id, tree, str_value_of_day)
            window.destroy()

    
    #EDIT OPTION
    def open_edit_window(self, window, tree, str_value_of_day):
        """
        [ENG] Method that allows the user to access more information about a task. If a task was not previously selected, it returns an error message instructing the user that to use the READ button they must first select a task from the list.
        --------
        [ESP] Método que permite al usuario acceder a mayor información sobre una tarea. Si no se seleccionó previamente una tarea, devuelve un mensaje de error indicando al usuario que para utilizar el boton READ primero debe seleccionar una tarea de la lista.
        """
        window.destroy()
        edit_window = Toplevel()
        edit_window.config(background='#FDEFFD')
        edit_window.title('Edit task')

        id = tree.selection()[0]
        values = self.handler.handler_read(id)
        name = values[0]
        date = values[1]
        type = values[2]
        desc = values[3]

        #Header
        self.show_header(edit_window)

        #Inputs
        task_name_label = Label(edit_window, text='Title: ')
        task_name_label.config(fg='#51141E', bg='#FDEFFD', font= ('Verdana', 10, 'bold'))
        task_name_label.configure(pady=3)
        task_name_label.grid(row=1, column=0)
        task_name_input = Entry(edit_window, textvariable = StringVar(edit_window, value=name))
        task_name_input.config(font= ('Verdana', 10, 'italic'))
        task_name_input.grid(row=1, column=1, columnspan=2)

        date_selected = StringVar(value=date)

        task_date_label = Label(edit_window, text='Date: ')
        task_date_label.config(fg='#51141E', bg='#FDEFFD', font= ('Verdana', 10, 'bold'))
        task_date_label.configure(pady=3)
        task_date_label.grid(row=2, column=0)
        task_date_input = Entry(edit_window, state=DISABLED, textvariable = date_selected)
        task_date_input.config(font= ('Verdana', 10, 'italic'))
        task_date_input.grid(row=2, column=1)

        self.calendar = PhotoImage(file='images/calendar.png').subsample(2)

        task_date_button = Button(edit_window, image=self.calendar, background='#FDEFFD', border=0, cursor = 'hand2', command= lambda: self.open_calendar(date_selected))
        task_date_button.grid(row=2, column=2)


        task_type_label = Label(edit_window, text='Type: ')
        task_type_label.config(fg='#51141E', bg='#FDEFFD', font= ('Verdana', 10, 'bold'))
        task_type_label.configure(pady=3)
        task_type_label.grid(row=3, column=0)
        task_type_input = ttk.Combobox(edit_window, state='readonly')
        task_type_input['values'] = ['Final exam', 'Midterm exam', 'Homework', 'Reading', 'Other']
        index_type = get_index(type)
        task_type_input.current(index_type)
        task_type_input.config(font= ('Verdana', 10, 'italic'))
        task_type_input.grid(row=3, column=1, columnspan=2)

        task_desc_label = Label(edit_window, text='Description: ')
        task_desc_label.config(fg='#51141E', bg='#FDEFFD', font= ('Verdana', 10, 'bold'))
        task_desc_label.configure(pady=3)
        task_desc_label.grid(row=4, column=0)
        task_desc_input = Text(edit_window, width=30, height=5)
        task_desc_input.config(font= ('Verdana', 10, 'italic'), borderwidth=3, relief='groove')
        task_desc_input.insert(END, desc)
        task_desc_input.grid(row=5, column=0, columnspan=3)    

        #Button
        save_button = Button(edit_window, text='SAVE', background='#198754', foreground='#fff', activebackground='#127C4B', font=('Verdana', 9), border=2, cursor = 'hand2', width=10, command=lambda: self.handler.handler_edit(id, task_name_input, task_date_input, task_type_input, task_desc_input, tree, edit_window, str_value_of_day))
        save_button.grid(row=6, column=0, sticky='we', columnspan=3)

        #Footer
        self.show_footer(edit_window, 7)

    def show_header(self, window):
        """
        [ENG] Method that displays the application header in each of the secondary windows.
        --------
        [ESP] Método que muestra el header de la aplicación en cada una de las ventanas secundarias.
        """
        self.secondary_header = PhotoImage(file='images/header_2.png').subsample(2)
        label_header = Label(window, image=self.secondary_header)
        label_header.grid(row=0, column=0, sticky='we', columnspan=3)

    def show_footer(self, window, row):
        """
        [ENG] Method that displays the application footer in each of the secondary windows.
        --------
        [ESP] Método que muestra el footer de la aplicación en cada una de las ventanas secundarias.
        """        
        footer_label = Label(window, text='Made with love by Solcii')
        footer_label.config(fg='white', bg='#9463AD', font=('Verdana', 7, 'italic'), borderwidth=5)
        footer_label.grid(row=row, column=0, sticky='we', columnspan=3)

from tkinter import Tk
from view import MyView


class MyApp:
    """
    [ENG] Class that acts as an application controller.
    --------
    [ESP] Clase que actúa como controlador de la aplicación.
    """
    def __init__(self, window):
        MyView(window)

if __name__ == "__main__":
    root = Tk()
    app = MyApp(root)
    root.mainloop()
    

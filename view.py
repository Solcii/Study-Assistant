from tkinter import Tk
from model import MyModel


class MyView:
    def __init__(self, window):
        self.window = window
        self.window.title('K.I.S.S.')
        Tk.iconbitmap(self.window, default='kicon.ico')
        self.window.config(background='#fafafa')


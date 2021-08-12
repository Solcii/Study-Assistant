from tkinter import Tk
from view import MyView


class MyApp:
    def __init__(self, window):
        self.window = window
        MyView(self.window)


if __name__ == "__main__":
    root = Tk()
    app = MyApp(root)
    root.mainloop()
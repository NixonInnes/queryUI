from tkinter import ttk


class BaseFrame:
    def __init__(self, parent, **callbacks):
        self.frame = ttk.Frame(parent)
        self.callbacks = callbacks
        self.setup()

    def setup(self):
        pass

    @property
    def height(self):
        return self.frame.winfo_height()

    @property
    def width(self):
        return self.frame.winfo_width()
   

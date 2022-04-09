import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

from ..options import Options
from .base import BaseFrame

options = Options(num_cols=2)


class EntryFrame(BaseFrame):
    def setup(self):
        url_label = ttk.Label(self.frame, text="URL")
        url_label.pack(side="left", **options.padding_title)

        self.url = tk.StringVar()
        url_entry = ttk.Entry(self.frame, textvariable=self.url)
        url_entry.pack(side="left", fill="x", expand=True, **options.padding)
        url_entry.focus()


class ParamsEntryFrame(BaseFrame):
    def setup(self):
        self.params = []
        self.param_entries = []

        label = ttk.Label(self.frame, text="Parameters")
        label.pack(fill="x", **options.padding_title)

        button_frame = ttk.Frame(self.frame)
        add_button = ttk.Button(button_frame, text="+")
        add_button.pack(side="left", **options.padding_tight)
        add_button.configure(command=self.add_param)

        sub_button = ttk.Button(button_frame, text="-")
        sub_button.pack(side="left", **options.padding_tight)
        sub_button.configure(command=self.sub_param)
        button_frame.pack(fill="x")

    def add_param(self):
        param_frame = ttk.Frame(self.frame)
        param_key = tk.StringVar()
        param_key_entry = ttk.Entry(param_frame, textvariable=param_key)
        param_key_entry.pack(side="left", fill="x", expand=True, **options.padding)
        param_value = tk.StringVar()
        param_value_entry = ttk.Entry(param_frame, textvariable=param_value)
        param_value_entry.pack(side="right", fill="x", expand=True, **options.padding)
        param_frame.pack(fill="both")
        self.params.append((param_key, param_value))
        self.param_entries.append((param_key_entry, param_value_entry, param_frame))

    def sub_param(self):
        if self.params:
            del self.params[-1]
            param_key_entry, param_value_entry, param_frame = self.param_entries.pop()
            param_key_entry.destroy()
            param_value_entry.destroy()
            param_frame.destroy()


class HeaderEntryFrame(BaseFrame):
    def setup(self):
        label = ttk.Label(self.frame, text="Headers")
        label.pack(fill="x", **options.padding_title)

        self.text = ScrolledText(self.frame, height=5)
        self.text.pack(fill="both", expand=True)


class DataEntryFrame(BaseFrame):
    def setup(self):
        label = ttk.Label(self.frame, text="Data")
        label.pack(fill="x", **options.padding_title)
        self.text = ScrolledText(self.frame, height=5)
        self.text.pack(fill="both", expand=True)

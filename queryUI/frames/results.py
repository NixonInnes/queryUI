import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

from ..options import Options
from ..utils import create_tooltip
from .base import BaseFrame


options = Options()

pretty_modes = ("TOML", "pprint")


class ResultsFrame(BaseFrame):
    def setup(self):
        self.label = ttk.Label(self.frame, text="Results")
        self.label.pack(fill="x")

        pretty_frame = tk.Frame(self.frame)

        self.pretty = tk.BooleanVar()
        self.pretty_check = ttk.Checkbutton(
            pretty_frame,
            text="Pretty",
            variable=self.pretty,
            onvalue=True,
            offvalue=False,
            command=self.callbacks["on_check"]
        )
        create_tooltip(self.pretty_check, "Try convert the result to TOML or pretty print")
        self.pretty_check.pack(side="left", **options.padding_tight)

        self.pretty_mode = tk.StringVar()
        self.pretty_mode.set(pretty_modes[0])
        self.pretty_mode_option = tk.OptionMenu(
            pretty_frame, 
            self.pretty_mode, 
            *pretty_modes,
            command=self.callbacks["on_check"]
        )
        self.pretty_mode_option.pack(side="right")
        pretty_frame.pack(fill="x")
        
        self.text = ScrolledText(self.frame)
        self.text.configure(state="disabled")
        self.text.pack(fill="both", expand=True)

    def set_content(self, content):
        self.text.configure(state="normal")
        self.text.delete("1.0", "end")
        self.text.insert("1.0", content)
        self.text.configure(state="disabled")

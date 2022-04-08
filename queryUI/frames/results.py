import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

from ..options import Options
from ..utils import create_tooltip
from .base import BaseFrame


options = Options()


class ResultsFrame(BaseFrame):
    def setup(self):
        self.label = ttk.Label(self.frame, text="Results")
        self.label.pack(fill="x")

        self.pretty = tk.BooleanVar()
        self.pretty_check = ttk.Checkbutton(
            self.frame,
            text="Pretty",
            variable=self.pretty,
            onvalue=True,
            offvalue=False
        )
        create_tooltip(self.pretty_check, "Try convert the result to TOML")
        self.pretty_check.pack(fill="x", **options.padding_tight)
        self.text = ScrolledText(self.frame)
        self.text.pack(fill="both", expand=True)

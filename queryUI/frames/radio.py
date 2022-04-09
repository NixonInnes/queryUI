import tkinter as tk
from tkinter import ttk

from ..options import Options
from .base import BaseFrame


radio_options = ("GET", "POST", "PUT", "DELETE")

options = Options(num_cols=len(radio_options))


class RadioFrame(BaseFrame):
    def setup(self):
        self.label = ttk.Label(self.frame, text="Method")
        self.label.pack(side="left", fill="x", **options.padding_title)

        self.selected = tk.StringVar()
        for i, option in enumerate(radio_options):
            radio = ttk.Radiobutton(
                self.frame,
                text=option,
                value=option.lower(),
                variable=self.selected,
            )
            radio.pack(side="left", **options.padding_tight)
        self.selected.set(radio_options[0].lower())

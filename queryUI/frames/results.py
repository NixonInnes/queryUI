import toml
import yaml
import json
from pprint import pformat

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showerror

from ..options import Options
from ..utils import create_tooltip
from .base import BaseFrame


options = Options()

pretty_modes = ("TOML", "pprint")

pretty_modes = {
    "TOML": toml.dumps,
    "YAML": yaml.dump,
    "pprint": pformat,
}


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
        create_tooltip(self.pretty_check, "Try to convert the data to the format selected (or just pretty print)")
        self.pretty_check.pack(side="left", **options.padding_tight)

        self.pretty_mode = tk.StringVar()
        self.pretty_mode.set("pprint")
        self.pretty_mode_option = tk.OptionMenu(
            pretty_frame, 
            self.pretty_mode, 
            *pretty_modes.keys(),
            command=self.callbacks["on_check"]
        )
        self.pretty_mode_option.pack(side="right")
        pretty_frame.pack(fill="x")
        
        self.text = ScrolledText(self.frame)
        self.text.configure(state="disabled")
        self.text.pack(fill="both", expand=True)


    def set_content(self, result_str):
        if self.pretty.get():
            # check if valid json
            try:
                dic = json.loads(result_str)
            except Exception as e:
                dic = None
                showerror(title="Error", message=f"{e!r}")

            if dic:
                try:
                    content = pretty_modes[self.pretty_mode.get()](dic)
                except Exception as e:
                    content = result_str
                    self.pretty.set(False)
                    showerror(title="Error", message=f"{e!r}")
            else:
                content = result_str
        else:
            content = result_str

        self.text.configure(state="normal")
        self.text.delete("1.0", "end")
        self.text.insert("1.0", content)
        self.text.configure(state="disabled")

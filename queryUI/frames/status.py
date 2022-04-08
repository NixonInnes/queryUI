import tkinter as tk

from .base import BaseFrame


class StatusFrame(BaseFrame):
    def setup(self):
        self.text = tk.StringVar()
        self.text.set("Ready for query")
        self.text_label = tk.Label(
            self.frame,
            textvariable=self.text,
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.text_label.pack(side="left", fill="x", expand=True)

        self.code = tk.StringVar()
        self.code.set("Status: None")
        self.code_label = tk.Label(
            self.frame,
            textvariable=self.code,
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.E
        )
        self.code_label.pack(side="right", fill="x", expand=True)

    def set_text(self, s: str):
        self.text.set(s)

    def set_code(self, s: str):
        self.code.set(f"Status: {s}")

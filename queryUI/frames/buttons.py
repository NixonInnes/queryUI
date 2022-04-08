import tkinter as tk

from ..options import Options
from .base import BaseFrame

options = Options()


class SubmitButtonFrame(BaseFrame):
    active_color = "SpringGreen"
    inactive_color = "SpringGreen2"

    def setup(self):
        self.submit_button = tk.Button(
            self.frame,
            text="Submit",
            bg=self.inactive_color,
            activebackground=self.active_color,
        )
        self.submit_button.pack(fill="x", **options.padding)
        self.submit_button.configure(command=self.callbacks["on_click"])


class SaveButtonsFrame(BaseFrame):
    save_active_color = "DeepSkyBlue"
    save_inactive_color = "DeepSkyBlue2"
    clip_active_color = "MediumPurple2"
    clip_inactive_color = "MediumPurple"

    def setup(self):
        self.save_button = tk.Button(
            self.frame,
            text="Save to File",
            bg=self.save_inactive_color,
            activebackground=self.save_active_color,
        )
        self.save_button.pack(side="left", **options.padding)
        self.save_button.configure(command=self.callbacks["on_click_save"])

        self.clip_button = tk.Button(
            self.frame,
            text="Copy to Clipboard",
            bg=self.clip_inactive_color,
            activebackground=self.clip_active_color,
        )
        self.clip_button.pack(side="right", **options.padding)
        self.clip_button.configure(command=self.callbacks["on_click_clip"])

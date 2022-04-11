import tkinter as tk
from tkinter.messagebox import showerror
from tkinter.filedialog import asksaveasfile

from .frames.radio import RadioFrame
from .frames.entry import EntryFrame, ParamsEntryFrame, HeaderEntryFrame, DataEntryFrame
from .frames.results import ResultsFrame
from .frames.buttons import SubmitButtonFrame, SaveButtonsFrame
from .frames.status import StatusFrame
from .options import Options
from .utils import parse_json_to_dict, query_url


options = Options()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("queryUI")
        self.last_result = None

        self.radio = RadioFrame(self)
        self.radio.frame.pack(fill="x", **options.padding_tight)

        self.entry = EntryFrame(self)
        self.entry.frame.pack(fill="x", **options.padding_tight)

        self.params = ParamsEntryFrame(self)
        self.params.frame.pack(fill="x", **options.padding_tight)

        self.header = HeaderEntryFrame(self)
        self.header.frame.pack(fill="x", **options.padding_tight)

        self.data = DataEntryFrame(self)
        self.data.frame.pack(fill="x", **options.padding_tight)

        self.submit = SubmitButtonFrame(self, on_click=self.submit_button_clicked)
        self.submit.frame.pack(fill="x", **options.padding_tight)

        self.results = ResultsFrame(self, on_check=self.update_results)
        self.results.frame.pack(fill="x", **options.padding_tight)

        self.save = SaveButtonsFrame(
            self, 
            on_click_save=self.save_button_clicked,
            on_click_clip=self.clipboard_button_clicked
        )
        self.save.frame.pack(fill="x", **options.padding_tight)

        self.status = StatusFrame(self)
        self.status.frame.pack(fill="x", side="bottom")

        self.bind("<Configure>", self.resize)
        self.geometry('1000x800+0+0')

    def submit_button_clicked(self):
        try:
            url = self.entry.url.get()
            method = self.radio.selected.get()
            params = {key.get(): value.get()
                      for key, value in self.params.params if key.get() != ""
                      }
            headers = parse_json_to_dict(
                self.header.text.get("1.0", "end"), field_name="Headers")
            data = parse_json_to_dict(
                self.data.text.get("1.0", "end"), field_name="Data")

            self.last_result = result = query_url(url, method, params=params,
                                                  data=data, headers=headers)
            self.update_results()
            self.status.set_text(f"{method.upper()} {result.url}")
            self.status.set_code(str(result.status_code))
        except Exception as e:
            showerror(title="Error", message=f"{e!r}")

    def save_button_clicked(self):
        try:
            file = asksaveasfile(
                mode="w",
                initialfile="response.txt",
                defaultextension=".txt",
                filetypes=[
                    ("All Files", "*.*"),
                    ("Text Documents", "*.txt"),
                    ("JSON Documents", "*.json"),
                    ("TOML Documents", "*.toml")
                ]
            )
            if file:
                file.write(self.results.text.get("1.0", "end"))
                file.close()
        except Exception as e:
            showerror(title="Error", message=f"{e!r}")

    def clipboard_button_clicked(self):
        self.clipboard_clear()
        self.clipboard_append(self.results.text.get("1.0", "end"))

    def update_results(self, event=None):
        if self.last_result is None:
            return
        self.results.set_content(self.last_result.content.decode())

    def resize(self, event):
        other_widgets_height = (
            self.radio.height + options.padding_tight["pady"]*2 +
            self.entry.height + options.padding_tight["pady"]*2 +
            self.params.height + options.padding_tight["pady"]*2 +
            self.header.height + options.padding_tight["pady"]*2 +
            self.data.height + options.padding_tight["pady"]*2 +
            self.submit.height + options.padding_tight["pady"]*2 +
            self.save.height + options.padding_tight["pady"]*2 +
            self.status.height
        )

        self.results.frame["height"] = int(
            # TODO: Figure out what im missing from other_widgets_height
            self.height - other_widgets_height) - 9
        self.results.frame["width"] = int(self.width)

    @property
    def height(self):
        return self.winfo_height()

    @property
    def width(self):
        return self.winfo_width()

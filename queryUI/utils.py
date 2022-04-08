import json
import requests
from typing import Dict, Optional

import tkinter as tk


class Row:
    def __init__(self):
        self.current = 0

    def next(self):
        self.current += 1
        return self.current


def query_url(
    url: str,
    method: str,
    params: Dict[str, str] = {},
    headers: str = "",
    data: str = ""
):
    func = getattr(requests, method)
    resp = func(url, params=params, headers=headers, data=json.dumps(data))
    return resp


def parse_json_to_dict(string: str, field_name: Optional[str] = None) -> dict:
    if string.strip() == "":
        return {}
    else:
        try:
            return json.loads(string)
        except:
            raise ValueError(
                f"Invalid JSON in{' '+field_name if field_name else ''} field")


class ToolTip:
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify="left",
                         background="#ffffe0", relief="solid", borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


def create_tooltip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

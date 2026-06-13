import tkinter as tk

class FieldButton(tk.Button):
    def __init__(self, master, field, text, on_click, **kwargs):
        super().__init__(master, text=text, command=on_click, **kwargs)
        self.field = field

class FieldLabel(tk.Label):
    def __init__(self, master, field, **kwargs):
        super().__init__(master, textvariable=field.trace_variable, **kwargs)
        self.field = field
import tkinter as tk

class ObservableField:
    def __init__(self, value):
        self._value = value
        # Simple tkinter trace wrapper mock
        self.trace_variable = tk.StringVar(value=str(value))
    
    @property
    def value(self):
        return self._value
        
    @value.setter
    def value(self, new_val):
        self._value = new_val
        self.trace_variable.set(str(new_val))

def init():
    pass
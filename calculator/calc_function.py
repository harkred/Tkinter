import tkinter as tk

def inserter(entry, element):
    entry.config(state='normal')
    entry.insert(tk.END, element)
    entry.config(state='readonly')
    
def dele(entry, lent):
    entry.config(state='normal')
    entry.delete(lent, tk.END)
    entry.config(state='readonly')
    
def clear(entry):
    entry.config(state='normal')
    entry.delete(0, tk.END)
    entry.config(state='readonly')
    
def calculate(entry):
    entry.config(state='normal')
    expression = entry.get()
    
    try: value = eval(expression)
    except Exception as e: value = 'Syntax error'
    
    entry.delete(0, tk.END)
    entry.insert(0, value)
    entry.config(state='readonly')
import tkinter as tk
from tkinter import ttk
import csv
from datetime import datetime

def deducter(frame, mframe):
    '''Deductor for deleting items from sub_frame'''
    
    for child in frame.winfo_children():
        child.destroy()
    frame.config(text='Add task details')
    adding_frame(frame, mframe)
    
def adder(frame, mframe):
    '''Bringing back original frame'''
    
    for child in mframe.winfo_children():
        child.destroy()
    
    from gui_frames import pending_window
    pending_window(mframe)

def adding_frame(frame, mframe):
    '''Data input frame'''
    
    ttk.Label(frame, text='Task Name: ').grid(row=0, column=0)
    ttk.Label(frame, text='Task Description: ').grid(row=1, column=0)
    ttk.Label(frame, text='Deadline(Date or time)').grid(row=2, column=0)
    
    name = ttk.Entry(frame, width=75)
    description = ttk.Entry(frame, width=75)
    deadline = ttk.Entry(frame, width=75)
    
    name.grid(row=0, column=1)
    description.grid(row=1, column=1)
    deadline.grid(row=2, column=1)
    
    btn_add = ttk.Button(frame, text='Add task', command=lambda:adder(frame, mframe))
    btn_add.grid(row=3, column=1)
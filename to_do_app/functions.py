import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox as msg
from datetime import datetime

#After the task has been done, this function to be used
def shove_frame(frame):
    for child in frame.winfo_children():
        child.destroy()
        
    
    #Task Frame
    task_frame = ttk.LabelFrame(frame, text='Your incomplete tasks')
    task_frame.grid(row=1, column=0, columnspan=2)

    #Buttons
    ttk.Button(frame, text='Add a task', command=lambda:add(frame)).grid(row=0, column=0, padx=10, pady=10)
    ttk.Button(frame, text='Finish task').grid(row=0, column=1, padx=10, pady=10)

    #ScrollBar
    task_scroll = ttk.Scrollbar(task_frame)

    #List box
    task_lst = tk.Listbox(task_frame, yscrollcommand=task_scroll.set, width=100)

    task_scroll.config(command=task_lst.yview)
    task_lst.pack(side=tk.LEFT)
    task_scroll.pack(side=tk.RIGHT, ipady=50)

#For adding to-do data
def add_task(frame, data):
    if len(data[1].get()) > 100: msg.showerror('', 'Description can\'t be greater than 100 characters')
    
    else:
        with open('tasks.csv', 'a') as file:
            data = list(map(lambda x: x.get(), data))
            data.append(datetime.date(datetime.utcnow()))
            
            write = csv.writer(file)
            write.writerow(data)
            
            msg.showinfo('', 'Data sucessfully added')
            
        shove_frame(frame)

def add(frame):
    for child in frame.winfo_children():
        child.destroy()
    
    frame.config(text='Add the task')
    
    #Labels
    ttk.Label(frame, text='Task Name: ').grid(row=0, column=0)
    ttk.Label(frame, text='Task Description: \n(Less than 100 charactes)').grid(row=1, column=0)
    ttk.Label(frame, text='Task Deadline: \n(Date/Time/Both)').grid(row=2, column=0)
    
    #Entries
    task_name = ttk.Entry(frame, width=100)
    task_desc = ttk.Entry(frame, width=100)
    task_deadline = ttk.Entry(frame, width=100)
    
    task_name.grid(row=0, column=1, ipady=5, columnspan=2)
    task_desc.grid(row=1, column=1, ipady=5, columnspan=2)
    task_deadline.grid(row=2, column=1, ipady=5, columnspan=2)
    
    #Buttons
    ttk.Button(frame, text='Add', command=lambda:add_task(frame, [task_name, task_desc, task_deadline])).grid(row=3, column=1)
    
    ttk.Button(frame, text='Discard', command=lambda:shove_frame(frame)).grid(row=3, column=2)
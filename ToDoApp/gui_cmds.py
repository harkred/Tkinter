import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from datetime import datetime
from csv_manager import store_data, retrieve_data

def deducter(frame, mframe):
    '''Deductor for deleting items from sub_frame'''
    
    for child in frame.winfo_children():
        child.destroy()
    frame.config(text='Add task details')
    adding_frame(frame, mframe)
    
def adder(frame, mframe, data):
    '''Bringing back original frame'''
    
    data = list(map(lambda x: x.get(), data))

    for datum in data:
        if datum == '':
            msg.showerror('', 'Please fill all the task details')
            break
    else:
        data.append(datetime.utcnow())
        store_data(data, 'a')
        msg.showinfo('', 'Task added')
        restorer(mframe)

def restorer(mframe):
    for child in mframe.winfo_children():
            child.destroy()
        
    from gui_frames import pending_window
    pending_window(mframe)

def adding_frame(frame, mframe):
    '''Data input frame'''
    
    ttk.Label(frame, text='Task Name: ').grid(row=0, column=0)
    ttk.Label(frame, text='Task Description: ').grid(row=1, column=0)
    ttk.Label(frame, text='Deadline(Date or time): ').grid(row=2, column=0)
    
    name = ttk.Entry(frame, width=75)
    description = ttk.Entry(frame, width=75)
    deadline = ttk.Entry(frame, width=75)
    
    name.grid(row=0, column=1, columnspan=2)
    description.grid(row=1, column=1, columnspan=2)
    deadline.grid(row=2, column=1, columnspan=2)
    
    data = [name, description, deadline]
    
    btn_add = ttk.Button(frame, text='Add task', command=lambda:adder(frame, mframe, data))
    btn_add.grid(row=3, column=1)
    
    btn_discard = ttk.Button(frame, text='Discard', command=lambda:restorer(mframe))
    btn_discard.grid(row=3, column=2)
    
def finish_task(lst):
    '''Finish a task'''
    data = [list(lst.get(i)) for i in lst.curselection()] #Gets selected tasks
    
    if len(data) == 0: msg.showerror('', 'Please select the task which is finished')
    
    else:
        new_data = retrieve_data() #New task initialisation
        
        for i in lst.curselection()[::-1]: #Remove finished tasks from tasks_list
            lst.delete(i)
        
        for datum in data: #Remove tasks from the database
            new_data.remove(datum)
            
        store_data(new_data, 'w')
        msg.showinfo('', f'Good job on completing {len(data)} tasks')
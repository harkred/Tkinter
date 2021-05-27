import tkinter as tk
from tkinter import ttk
from gui_cmds import deducter

def main_window(root):
    '''Main Window'''
    global main_frame
    main_frame = ttk.LabelFrame(root, text='To Do App')
    main_frame.pack(fill='both', expand=1)
    
    pending_window(main_frame)
    
    tk.mainloop()

def pending_window(frame):
    '''Pending Window'''

    sub_frame = ttk.LabelFrame(frame, text='Pending Tasks')
    sub_frame.pack(fill='both', expand=1)
    
    btn_add = ttk.Button(sub_frame, text='Add task', command=lambda:deducter(sub_frame, main_frame))
    btn_add.grid(row=0, column=0)
    
    btn_finish = ttk.Button(sub_frame, text='Finish Tasks')
    btn_finish.grid(row=0, column=1)
    
    tasks_list = tk.Listbox(sub_frame, selectmode=tk.MULTIPLE, width=100)
    tasks_list.grid(row=1, column=0, columnspan=2)
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from functions import add

root = ThemedTk()

#Main Frame
main_frame = ttk.LabelFrame(root, text='To Do app')
main_frame.pack(fill=tk.BOTH, expand=1)

#Task Frame
task_frame = ttk.LabelFrame(main_frame, text='Your incomplete tasks')
task_frame.grid(row=1, column=0, columnspan=2)

#Buttons
ttk.Button(main_frame, text='Add a task', command=lambda:add(main_frame)).grid(row=0, column=0, padx=10, pady=10)
ttk.Button(main_frame, text='Finish task').grid(row=0, column=1, padx=10, pady=10)

#ScrollBar
task_scroll = ttk.Scrollbar(task_frame)

#List box
task_lst = tk.Listbox(task_frame, yscrollcommand=task_scroll.set, width=100)

task_scroll.config(command=task_lst.yview)
task_lst.pack(side=tk.LEFT)
task_scroll.pack(side=tk.RIGHT, ipady=50)

tk.mainloop()
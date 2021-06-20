import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from calc_function import inserter, dele, clear, calculate

root = ThemedTk()
root.set_theme('aquativo')
root.resizable(0, 0)

#Main frame
main_frame = ttk.LabelFrame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

#Entry
entry = ttk.Entry(main_frame, state='readonly', width=80)
entry.grid(row=0, column=0, columnspan=5, ipady=5)

#Buttons
#Numbers
button1 = ttk.Button(main_frame, text='1', command=lambda:inserter(entry, 1))
button2 = ttk.Button(main_frame, text='2', command=lambda:inserter(entry, 2))
button3 = ttk.Button(main_frame, text='3', command=lambda:inserter(entry, 3))

button4 = ttk.Button(main_frame, text='4', command=lambda:inserter(entry, 4))
button5 = ttk.Button(main_frame, text='5', command=lambda:inserter(entry, 5))
button6 = ttk.Button(main_frame, text='6', command=lambda:inserter(entry, 6))

button7 = ttk.Button(main_frame, text='7', command=lambda:inserter(entry, 7))
button8 = ttk.Button(main_frame, text='8', command=lambda:inserter(entry, 8))
button9 = ttk.Button(main_frame, text='9', command=lambda:inserter(entry, 9))

button0 = ttk.Button(main_frame, text='0', command=lambda:inserter(entry, 0))

#Operations
button_plus = ttk.Button(main_frame, text='+', command=lambda:inserter(entry, '+'))
button_minus = ttk.Button(main_frame, text='-', command=lambda:inserter(entry, '-'))

button_multiply = ttk.Button(main_frame, text='*', command=lambda:inserter(entry, '*'))
button_divide = ttk.Button(main_frame, text='/', command=lambda:inserter(entry, '/'))

button_expo = ttk.Button(main_frame, text='**', command=lambda:inserter(entry, '**'))
button_mod = ttk.Button(main_frame, text='%', command=lambda:inserter(entry, '%'))

#Deleteing
button_del = ttk.Button(main_frame, text='DEL', command=lambda:dele(entry, len(entry.get())-1))
button_clear = ttk.Button(main_frame, text='C', command=lambda:clear(entry))

#Output
button_equal = ttk.Button(main_frame, text='=', command=lambda:calculate(entry))

#Buttons shovin
#Numbers
button1.grid(row=1, column=0, ipadx=30, padx=5, pady=10)
button2.grid(row=1, column=1, ipadx=30)
button3.grid(row=1, column=2, ipadx=30)

button4.grid(row=2, column=0, ipadx=30, padx=5, pady=10)
button5.grid(row=2, column=1, ipadx=30)
button6.grid(row=2, column=2, ipadx=30)

button7.grid(row=3, column=0, ipadx=30, padx=5, pady=10)
button8.grid(row=3, column=1, ipadx=30)
button9.grid(row=3, column=2, ipadx=30)

button0.grid(row=4, column=0, ipadx=30, padx=5, pady=10)

#Operations
button_multiply.grid(row=2, column=3, ipadx=30)
button_divide.grid(row=2, column=4, ipadx=30)

button_plus.grid(row=3, column=3, ipadx=30)
button_minus.grid(row=3, column=4, ipadx=30)

button_expo.grid(row=4, column=1, ipadx=30)
button_mod.grid(row=4, column=2, ipadx=30)

#Deleting
button_del.grid(row=1, column=3, ipadx=30)
button_clear.grid(row=1, column=4, ipadx=30)

#Output
button_equal.grid(row=4, column=3, ipadx=75, columnspan=2)

root.mainloop()
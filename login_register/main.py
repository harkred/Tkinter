import tkinter as tk
from tkinter import ttk
from function import registering, loggin, forget_details

root = tk.Tk()
root.resizable(0, 0)

#Main Frame
main_frame = ttk.LabelFrame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

#Tabs
tab = ttk.Notebook(main_frame)
tab.pack(side='left', anchor=tk.N)

#Login
login = ttk.Frame(main_frame)
login.pack(side='left')

#Register
register = ttk.Frame(main_frame)
register.pack(side='right')

tab.add(login, text='Login')
tab.add(register, text='Sign Up')

#Login Components
ttk.Label(login, text='Username: ').grid(row=0, column=0)
ttk.Label(login, text='Password: ').grid(row=1, column=0)

login_username = ttk.Entry(login, width=35)
login_password = ttk.Entry(login, width=35)

login_username.grid(row=0, column=1, columnspan=2, pady=5)
login_password.grid(row=1, column=1, columnspan=2, pady=5)

ttk.Button(login, text='Forgot Username/Password', command=forget_details).grid(row=2, column=0, columnspan=3, pady=10)
ttk.Button(login, text='Login', command=lambda:loggin(login_username, login_password)).grid(row=3, column=1, pady=10)

#Register components
ttk.Label(register, text='Username: ').grid(row=0, column=0)
ttk.Label(register, text='Password: ').grid(row=1, column=0)
ttk.Label(register, text='Email: ').grid(row=2, column=0)

signup_username = ttk.Entry(register, width=35)
signup_password = ttk.Entry(register, width=35)
signup_email = ttk.Entry(register, width=35)

signup_username.grid(row=0, column=1, columnspan=2, pady=2)
signup_password.grid(row=1, column=1, columnspan=2, pady=2)
signup_email.grid(row=2, column=1, columnspan=2, pady=2)

ttk.Button(register, text='Sign Up!', command=lambda:registering(signup_username, signup_password, signup_email)).grid(row=4, column=1, pady=2)

tk.mainloop()
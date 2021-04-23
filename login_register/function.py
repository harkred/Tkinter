import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import pickle
import re

def username_validator(username):
    with open('user_data.dat', 'rb') as users:
        try:
            while True:
                data = pickle.load(users)
                if username in data.keys():
                    msg.showerror('', 'Username already exists')
                    return 0
                    
        except EOFError:
            return 1

def field_validator(*args):
    space_regex = r'[\s]+'
    email_regex = r'^[\w\d]+@[\w]+\.com$'
    
    for field in args:
        if(field.get().rstrip() == ''):
            msg.showerror('', 'Please fill all the fields')
            break
            
        if(re.search(space_regex, field.get().rstrip()) and args.index(field) == 2):
            msg.showerror('', 'Please remove spaces')
            break
    
    else:
        if(re.match(email_regex, args[2].get().rstrip()) and username_validator(args[0].get()) == 1):
            dictionary = {
                args[0].get(): [args[1].get(), args[2].get()]
            }
            return dictionary
        else:
            msg.showerror('', 'Use appropriate email')

def registering(*args):
    if field_validator(*args) is None:
        pass
    else:
        with open('user_data.dat', 'ab') as users:
            pickle.dump(field_validator(*args), users)
            
            for field in args:
                field.delete(0, tk.END)
            
            msg.showinfo('', 'Sign up sucessfull')
            
def loggin(*args):
    with open('user_data.dat', 'rb') as users:
        try:
            while True:
                data = pickle.load(users)
                if(data.get(args[0].get(), '@@q')[0] == args[1].get()):
                    msg.showinfo('Sucessfully loggined', f'Welcome back {args[0].get()}')
                    args[0].delete(0, tk.END)
                    args[1].delete(0, tk.END)
                    
                    return 1
                    
        except EOFError:
            msg.showerror('', 'Invalid username/password')
            return 0
            
def forget_details():
    def send():
        email_regex = r'^[\w\d]+@[\w]+\.com$'
        
        if(re.match(email_regex, email.get())):
            msg.showinfo('', 'Email has been sent')
            win.destroy()
            return
            
        msg.showerror('', 'Please fill appropriate email')

    win = tk.Tk()
    win.resizable(0, 0)
    
    ttk.Label(win, text='Please enter your email: ').grid(row=0, column=0, pady=10)
    
    email = ttk.Entry(win, width=35)
    email.grid(row=0, column=1, columnspan=2, pady=10)
    
    ttk.Button(win, text='Send', command=send).grid(row=1, column=1)
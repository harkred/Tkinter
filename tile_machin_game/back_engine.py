import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import time
import threading

checker = []
btns = []
completed = []

def start_time(progress):
    '''Start time'''
    while progress['value'] > 0:
        progress['value'] -= 1
        time.sleep(1)
    
    msg.showerror('', 'You lost the game')

def tile_matcher(btn, value):
    '''Tile matcher'''
    global checker, btns
    btn.config(text=str(value))
    btn.config(state=tk.DISABLED)
    
    checker.append(value)
    btns.append(btn)
    
    if len(checker) == 2:
        if checker[0] == checker[1]:
            t = threading.Thread(target=if_match)
            t.setDaemon(True)
            t.start()
        
        else:
            t = threading.Thread(target=ifnot_match)
            t.setDaemon(True)
            t.start()

def if_match():
    '''To check if tile matches'''
    global checker, btns, completed
    
    completed.extend(btns)
    
    time.sleep(0.3)
    for _btn in btns:
        _btn.config(text='-------', state=tk.DISABLED)
        checker = []
        btns = []
    
    if len(completed) == 10: msg.showinfo('', 'Yay!! You have won the game')

def ifnot_match():
    '''If tile does not matches'''
    global checker, btns
    
    time.sleep(0.5)
    for _btn in btns:
        _btn.config(text='?')
        _btn.config(state=tk.NORMAL)
        checker = []
        btns = []
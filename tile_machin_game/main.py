import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import time
import threading
import random
from back_engine import start_time, tile_matcher

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Tile maching game')
    root.resizable(0,0)

    #WARNING!!!
    msg.showwarning('Note:', 'Please play the game slowly and do not match tiles in a hurry so as to avoid any types of glitches')

    #main frame
    main_frame = ttk.LabelFrame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    #Buttons
    values = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

    value1 = random.choice(values)
    button1 = ttk.Button(main_frame, text='?', command=lambda:tile_matcher(root, button1, value1))
    values.remove(value1)

    value2 = random.choice(values)
    button2 = ttk.Button(main_frame, text='?', command=lambda:tile_matcher(root, button2, value2))
    values.remove(value2)

    value3 = random.choice(values)
    button3 = ttk.Button(main_frame, text='?', command=lambda:tile_matcher(root, button3, value3))
    values.remove(value3)

    value4 = random.choice(values)
    button4 = ttk.Button(main_frame, text='?', command=lambda:tile_matcher(root, button4, value4))
    values.remove(value4)

    value5 = random.choice(values)
    button5 = ttk.Button(main_frame, text='?', command=lambda:tile_matcher(root, button5, value5))
    values.remove(value5)

    value6 = random.choice(values)
    button6 = ttk.Button(main_frame, text='?', command=lambda:tile_matcher(root, button6, value6))
    values.remove(value6)

    value7 = random.choice(values)
    button7 = ttk.Button(main_frame, text='?', command=lambda:tile_matcher(root, button7, value7))
    values.remove(value7)

    value8 = random.choice(values)
    button8 = ttk.Button(main_frame, text='?', command=lambda:tile_matcher(root, button8, value8))
    values.remove(value8)

    value9 = random.choice(values)
    button9 = ttk.Button(main_frame, text='?', command=lambda:tile_matcher(root, button9, value9))
    values.remove(value9)

    value10 = random.choice(values)
    button10 = ttk.Button(main_frame, text='?', command=lambda:tile_matcher(root, button10, value10))
    values.remove(value10)

    #Button list
    btn_lst = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10]

    #Button shovin to screen
    button1.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=20)
    button2.grid(row=0, column=1, padx=10, pady=10, ipadx=20, ipady=20)
    button3.grid(row=0, column=2, padx=10, pady=10, ipadx=20, ipady=20)
    button4.grid(row=0, column=3, padx=10, pady=10, ipadx=20, ipady=20)
    button5.grid(row=0, column=4, padx=10, pady=10, ipadx=20, ipady=20)
    button6.grid(row=1, column=0, padx=10, pady=10, ipadx=20, ipady=20)
    button7.grid(row=1, column=1, padx=10, pady=10, ipadx=20, ipady=20)
    button8.grid(row=1, column=2, padx=10, pady=10, ipadx=20, ipady=20)
    button9.grid(row=1, column=3, padx=10, pady=10, ipadx=20, ipady=20)
    button10.grid(row=1, column=4, padx=10, pady=10, ipadx=20, ipady=20)

    #time left
    track_time = ttk.Progressbar(main_frame, length=500, mode='determinate')
    track_time.grid(row=2, column=0, columnspan=5)

    track_time['value'] = 100
    t = threading.Thread(target = start_time, args=[track_time])
    t.setDaemon(True)
    t.start()

    tk.mainloop()
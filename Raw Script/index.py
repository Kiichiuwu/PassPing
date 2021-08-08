from random import setstate
from tkinter.constants import DISABLED, LEFT
from typing import Counter, Text
from passwordgn import *
import tkinter as tk

#janela

class Root(tk.Tk):
    def __init__(self):
        super (Root, self).__init__()
        self.title("PassPing V1.0")
        self.configure(background = '#4D4D4D')
        photo = tk.PhotoImage(file = "icon2.png")
        self.iconphoto(False, photo)
        label = tk.Label(text=('*** PassPing © 2021 Kiichi ***'), width= 35, background='#4D4D4D', fg='#FF0000').pack()
        label = tk.Label(text=('Thank you fo choosing PassPing.'), width= 35, background='#4D4D4D', fg='#FF0000').pack()
        label = tk.Label(width= 35, background='#4D4D4D', fg='#FF0000').pack()
        label = tk.Label(text=('Your Password is:'), width= 35, background='#4D4D4D', fg='#FF0000').pack()
        label = tk.Label(text=(password), width= 35, background='#4D4D4D', fg='#39FF14').pack()
        label = tk.Label(width= 35, background='#4D4D4D', fg='#FF0000').pack()
        button = tk.Button(text='Copy Password', command=copytoclip, width=35).pack()
        button2 = tk.Button(text='Save Password', command=savepass, width=35).pack()
    pass
#definições

def copytoclip():
    plin = tk.Tk()
    plin.withdraw()
    plin.clipboard_clear()
    plin.clipboard_append(password)
pass

def savepass():
    file = open("Pass.txt", "a")
    file.write(f"password: {password} \n")
    file.close()
    exit()
pass

root = Root()
root.mainloop()
#!/usr/bin/env python3
from tkinter import * 
import random
from tkinter.messagebox import* 

root = Tk();
root.title('Вірус');
root.geometry('600x400+300+300');
root['bg']='#40E0D0';

windows = [];
def click (event):
    showerror('Помилка', 'Ви натрапили на вірус!');

def close ():
    newWindow = Tk();
    newWindow.title('Вірус');
    newWindow.geometry(f'600x400+{random.randint(1, 500)}+{random.randint(1, 500)}');
    newWindow['bg']='#40E0D0';
    newWindow.bind('<1>', click);
    newWindow.protocol("WM_DELETE_WINDOW", close);
    windows.append(newWindow);


root.bind('<1>', click);
root.protocol("WM_DELETE_WINDOW", close);
root.mainloop();
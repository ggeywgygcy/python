from tkinter import *
from datetime import datetime as dt

def insert_time():
    time = dt.now().time()
    e1.insert(END,time.strftime('%H:%M:%S   '))

window = Tk()
e1 = Entry(width=50)
b1= Button(text='Время',command=insert_time)

e1.pack()
b1.pack()

window.mainloop()
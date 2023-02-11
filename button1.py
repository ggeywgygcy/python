from tkinter import *

def change():
    button1['text'] = 'Изменено...'
    button1['bg'] = '#000000'
    button1['activebackground'] = '#555555'
    button1['fg'] = '#ffffff'
    button1['activebackground'] = '#ffffff'

window = Tk()

button1 = Button(text="Изменить",width=15,height=100)

button1.config(command=change)

button1.pack()

root = mainloop()
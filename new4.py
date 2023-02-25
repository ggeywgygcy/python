from tkinter import *

def smile():
    l = Label(text='5',bg='#000000')
    text.window_create(INSERT,window=l)

root = Tk()

text = Text(width=50,height=10)
text.pack()

button = Button(text='5',command=smile)
button.pack()

root.mainloop()
from tkinter import *

def change():
    label['text'] = 'Выдано'

window = Tk()

Label(text='Пункт выдачи').pack()
Button(text='Получить',command=change).pack()

label = Label(width=10,height=1)

label.pack()

window.mainloop()
from tkinter import *

root = Tk()

def insert_text():
    s = 'Привет Мир'
    text.insert(1.0,s)

def get_text():
    s = text.get(1.0,END)
    l['text'] = S

def delete_text():
    text.delete(1.0,END)

text = Text(width=20,height=7)
text.pack()

frame = Frame()
frame.pack()
Button(frame,text='Вставить',command=insert_text).pack(side=LEFT)
Button(frame,text='Взять',command=get_text).pack(side=LEFT)
Button(frame,text='Удалить',command=delete_text).pack(side=LEFT)

l = Label()
l.pack()



root.mainloop()
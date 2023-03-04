from tkinter import *

def proverka():
    if rVar.get() == 0:
        l1['text'] = 'первый'
    elif rVar.get() == 1:
        l1['text'] = 'второй'

root = Tk()

rVar = BooleanVar()
rVar.set(0)



r1 = Radiobutton(text='Первый',variable=rVar,value=0)
r2 = Radiobutton(text='Второй',variable=rVar,value=1)

l1 = Label(width=50)

b1 = Button(text='Проверить выбор', command=proverka)

r1.pack()
r2.pack()
l1.pack()
b1.pack()

root.mainloop()
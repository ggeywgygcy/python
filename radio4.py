from tkinter import *

def proverka():
    if rVar.get() == 0:
        l1['bg'] = '#FFCC00'
    elif rVar.get() == 1:
        l1['bg'] = 'red'
    elif rVar.get() == 2:
        l1['bg'] = '#8B00FF'

root = Tk()

rVar = IntVar()
rVar.set(0)



r1 = Radiobutton(text='Яндекса',variable=rVar,value=0,command=proverka)
r2 = Radiobutton(text='Красный',variable=rVar,value=1,command=proverka)
r3 = Radiobutton(text='Фиолетовый',variable=rVar,value=2,command=proverka)
l1 = Label(width=20,height=10)
#b1 = Button(text='Изменить', command=proverka)

r3.pack()
r1.pack()
r2.pack()
l1.pack()
#b1.pack()

root.mainloop()
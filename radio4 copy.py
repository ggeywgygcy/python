from tkinter import *

def proverka():
    if rVar.get() == 0:
        l1['text'] = '+884759848598'
    elif rVar.get() == 1:
        l1['text'] = '+76474637568'
    elif rVar.get() == 2:
        l1['text'] = '7575956549645'

root = Tk()

rVar = IntVar()
rVar.set(0)



r1 = Radiobutton(text='Маша',variable=rVar,value=0,command=proverka,indicatoron=0)
r2 = Radiobutton(text='Петя',variable=rVar,value=1,command=proverka,indicatoron=0)
r3 = Radiobutton(text='Вася',variable=rVar,value=2,command=proverka,indicatoron=0)
l1 = Label(width=20,height=10)
#b1 = Button(text='Изменить', command=proverka)

l1.pack()
r3.pack(side=LEFT)
r1.pack(side=LEFT)
r2.pack(side=LEFT)

#b1.pack()

root.mainloop()
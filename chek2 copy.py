from tkinter import *
from tkinter.ttk import *
   

def toSecond():
    selectToSecond = list(lbox1.curselection())
    selectToSecond.reverse()
    lbox2.insert(END, selectToSecond.get())
    for i in lbox1:
        lbox1.delete(i)

def toFirst():
    selectToFirst = list(lbox2.curselection())
    selectToFirst.reverse()
    lbox1.insert(END, selectToFirst.get())
    for i in lbox2:
        lbox2.delete(i)


root = Tk()

lbox1 = Listbox(selectmode=EXTENDED)

for i in ('Груша','Картошка','Мясо','Масло','Хлеб','Морковь','Банан','Яблоко'):
    lbox1.insert(0,i)

lbox1.pack(side=LEFT)

lbox2 = Listbox(selectmode=EXTENDED)
lbox2.pack(side=RIGHT)

f = Frame()
f.pack(side=LEFT, padx=10)
Button(f, text=">>>", command=toSecond).pack(fill=X)
Button(f, text="<<<", command=toFirst).pack(fill=X)

root.mainloop()



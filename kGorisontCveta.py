from tkinter import *

def button1():
    a1['text'] = 'Красный'
    b1.delete(0,END)
    b1.insert(0,'#ff0000')

def button2():
    a1['text'] = 'Оранжевый'
    b1.delete(0,END)
    b1.insert(0,'#ff7d00')

def button3():
    a1['text'] = 'Желтый'
    b1.delete(0,END)
    b1.insert(0,'#ffff00')

def button4():
    a1['text'] = 'Зеленый'
    b1.delete(0,END)
    b1.insert(0,'#00ff00')

def button5():
    a1['text'] = 'Голубой'
    b1.delete(0,END)
    b1.insert(0,'#007dff')

def button6():
    a1['text'] = 'Синий'
    b1.delete(0,END)
    b1.insert(0,'#0000ff')

def button7():
    a1['text'] = 'Фиолетовый'
    b1.delete(0,END)
    b1.insert(0,'#7d00ff')

root = Tk()

fr = Frame(root)

a1 = Label(width=50,anchor=CENTER)
b1 = Entry(width=50,justify=CENTER)
l1 = Button(fr,width=50,command=button1,bg='#ff0000')
l2 = Button(fr,width=50,command=button2,bg='#ff7d00')
l3 = Button(fr,width=50,command=button3,bg='#ffff00')
l4 = Button(fr,width=50,command=button4,bg='#00ff00')
l5 = Button(fr,width=50,command=button5,bg='#007dff')
l6 = Button(fr,width=50,command=button6,bg='#0000ff')
l7 = Button(fr,width=50,command=button7,bg='#7d00ff')

a1.pack()
b1.pack()
l1.pack()
l2.pack()
l3.pack()
l4.pack()
l5.pack()
l6.pack()
l7.pack()

fr.pack()


root.mainloop()
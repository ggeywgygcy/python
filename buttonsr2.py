from tkinter import *

def button1():
    b1['text'] = 'Изменено...'
    b1['bg'] = '#ff0000'
    l1['text'] = 'красный'
    b1.config(command=button1)

def button2():
    b2['text'] = 'Изменено...'
    b2['bg'] = '#ff7d00'
    l2['text'] = 'оранжевый'


def button3():    
    b3['text'] = 'Изменено...'
    b3['bg'] = '#ffff00'
    l3['text'] = 'желтый'


def button4():
    b4['text'] = 'Изменено...'
    b4['bg'] = '#00ff00'
    l4['text'] = 'зеленый'


def button5():
    b5['text'] = 'Изменено...'
    b5['bg'] = '#007dff'
    l5['text'] = 'красный'

def button6():
    b6['text'] = 'Изменено...'
    b6['bg'] = '#0000ff'
    l6['text'] = 'красный'

def button7():
    b7['text'] = 'Изменено...'
    b7['bg'] = '#7d00ff'
    l7['text'] = 'красный'

root = Tk()

b1 = Button(text="Изменить",width=15,height=1)
b2 = Button(text="Изменить",width=15,height=1)
b3 = Button(text="Изменить",width=15,height=1)
b4 = Button(text="Изменить",width=15,height=1)
b5 = Button(text="Изменить",width=15,height=1)
b6 = Button(text="Изменить",width=15,height=1)
b7 = Button(text="Изменить",width=15,height=1)

l1 = Label(text="Изменить",width=15,height=1)
l2 = Label(text="Изменить",width=15,height=1)
l3 = Label(text="Изменить",width=15,height=1)
l4 = Label(text="Изменить",width=15,height=1)
l5 = Label(text="Изменить",width=15,height=1)
l6 = Label(text="Изменить",width=15,height=1)
l7 = Label(text="Изменить",width=15,height=1)


b2.config(command=button2)
b3.config(command=button3)
b4.config(command=button4)
b5.config(command=button5)
b6.config(command=button6)
b7.config(command=button7)

l1.config(command=button1)
l2.config(command=button2)
l3.config(command=button3)
l4.config(command=button4)
l5.config(command=button5)
l6.config(command=button6)
l7.config(command=button7)

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()

l1.pack()
l2.pack()
l3.pack()
l4.pack()
l5.pack()
l6.pack()
l7.pack()

root.mainloop()
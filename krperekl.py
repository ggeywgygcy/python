from tkinter import *

def proverka(color):
    label['bg'] = color

class RBColor:
    def __init__(self,color,val):
        Radiobutton(
            text=color,
            command=lambda i=color: proverka(i),
            variable=rVar,value=val
        ).pack()

root = Tk()

rVar = IntVar()
rVar.set(0)

RBColor('#FFCC00',0)
RBColor('red',1)
RBColor('#8B00FF',2)


label = Label(width=20,height=10,bg='red')

label.pack()


root.mainloop()
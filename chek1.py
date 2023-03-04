from tkinter import *

def show():
    s = f'{var1.get()},' \
        f'{var2.get()}'
    

root = Tk()

frame = Frame()
frame.pack()

var1 = BooleanVar()
var1.set(0)

c1 = Checkbutton(frame,text='One',
                 variable=var1,
                 onvalue=1,offvalue=0,
                 command=show)
c1.pack(anchor=W,padx=10)

var2 = IntVar()
var2.set(-1)

c2 = Checkbutton(frame,text='Tou',
                 variable=var2,
                 onvalue=1,offvalue=0,
                 command=show)
c2.pack(anchor=W,padx=10)

label = Label(width=25,height=5)
label.pack(side=RIGHT)


root.mainloop()
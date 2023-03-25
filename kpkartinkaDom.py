from tkinter import *

root = Tk()

c = Canvas(root, width=300, height=300, bg='white')
c.pack()

c.create_polygon(100, 10, 20, 90, 180, 90)

c.create_rectangle(55, 75, 135, 185,
                   fill='black',
                   width=3,
                   activedash=(5, 4))

c.create_oval(150, 10, 190, 50,
              fill='#EDFF21')

x = -20
while x<200:
    c.create_arc(x,170,x+40,250,outline='green',
                 style=ARC,start=100,extent=80,
                 width=2)
    x += 10

root.mainloop()
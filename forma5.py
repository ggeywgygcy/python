from tkinter import *
from forma3 import creat_triangle

root = Tk()
root.title('Треугльник')
canvas = Canvas(root,width=800,height=600,background='white')
creat_triangle(canvas,100,50,100,200,400,200)
canvas.pack(expand=True,fill=BOTH)
root.mainloop() 
from tkinter import *
from forma3 import creat_triangle

root = Tk()
root.title('Треугльник')
canvas = Canvas(root,width=800,height=600,background='white')
creat_triangle(input('Введите координату x для первой вершины '))
canvas.pack(expand=True,fill=BOTH)
root.mainloop() 
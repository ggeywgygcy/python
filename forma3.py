from tkinter import *

def creat_triangle(canvas,x1,y1,x2,y2,x3,y3):
    
    
    х1 = input('введите первую координату для х1 ')
    y1 = input('введите вторую координату для х1 ')
    canvas.create_line(x1,y1,x2,y2)
    
    х2 = input('введите первую координату для х2 ')
    y2 = input('введите вторую координату для х2 ')
    canvas.create_line(x1,y1,x3,y3)
    
    х3 = input('введите первую координату для х3 ')
    y3 = input('введите вторую координату для х3 ')

    canvas.create_line(x3,y3,x2,y2)
   
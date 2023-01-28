from tkinter import *
from tkinter import ttk

from tkinter import *
from tkinter import ttk
 
clicks = 0

def click_button():
    global clicks
    clicks +=1
    
    if clicks == 1:
        btn["text"] = f" Малинин Данил  {clicks}"
    
    elif clicks == 2:
        btn["text"] = f" Шинин Егор  {clicks}"

    elif clicks == 3:
        btn["text"] = f" Шеронов Егор  {clicks}"

    else:
        btn["text"] = f" Никого больше нету  {clicks}"
        btn["state"] = [DISABLED]
    
    
root = Tk()
root.title('Rjjjjj')
root.geometry("250x150")
 
btn = ttk.Button(text="Нажми меня", command=click_button)
btn.pack()
 
root.mainloop() 
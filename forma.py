from tkinter import *
from tkinter import ttk

click = 0

def click_button():
    global click
    click +=1
    btn["text"] = f"Нажатие{click}"


window = Tk()
window.title("Кнопка. ")
window.geometry('100x600')

btn = ttk.Button(text="Нажми мня", command=click_button)
btn.pack()

window.mainloop











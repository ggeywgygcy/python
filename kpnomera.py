'''Напишите программу, в которой имеется несколько объединенных в группу радиокнопок,
индикатор которых выключен (indicatoron=0). Если какая-нибудь кнопка включается, то в
метке должна отображаться соответствующая ей информация. Обычных кнопок в окне быть
не должно.'''

from tkinter import *

#Словарь с данными людей
persons = {
    'Петя': '+49084968696t856553325',
    'Вася': '+290844745653764755339',
    'Маша': '+19348655675856484453325',}

#Установка информации о человеке в label
def get_info():
    label.config(text=persons[var.get()])

root = Tk()
root.title('Информация о сотруднике')
root.resizable(height=False, width=False)

f_left = Frame(root)
f_left.pack(side=LEFT)

label = Label(root, justify='center', width=40, text='', font=18)
label.pack(side=LEFT, expand=True)

var = StringVar()

for name in persons.keys():
    Radiobutton(f_left, width=20, font = 20, text=name, indicatoron=0, variable=var,
        value=name, command=get_info).pack(side=TOP)

root.mainloop()
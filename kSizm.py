from tkinter import *

root = Tk()

Label(text='ИМя: ').grid(row=0, column=0)
table_name = Entry()
table_name.grid(row=0, column=1, columnspan=3, sticky=W+E, padx=10)

Label(text="Столбцов: ").grid(row=1, column=0, sticky=W, padx=10, pady=10)
Spinbox(width=7, from_=1, to=50).grid(row=1, column=1, padx=10)

Label(text='Строк').grid(row=1, column=2, sticky=E)
Spinbox(width=7, from_=1, to=100).grid(row=1, column=3, sticky=E, padx=10)

Button(text='Spravka').grid(row=2,column=2)
 
root.mainloop()
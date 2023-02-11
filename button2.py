from tkinter import *

window = Tk()

label1 = Label(text='Машинное обучение',font='Arial 32')
label2 = Label(text='Распознание образов',font=('Khmer OS',24,'bold'))

label1.config(bd=20, bg='#ffaaaa')
label2.config(bd=20, bg='#aaffff')

label1.pack()
label2.pack()

window.mainloop()
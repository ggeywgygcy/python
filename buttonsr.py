from tkinter import *

def change():
    b1['text'] = 'Каждый'
    b1['bg'] = '#ff0000'

    b2['text'] = 'охотник'
    b2['bg'] = '#ff7d00'
    
    b3['text'] = 'желает'
    b3['bg'] = '#ffff00'

    b4['text'] = 'знать'
    b4['bg'] = '#00ff00'

    b5['text'] = 'где'
    b5['bg'] = '#007dff'

    b6['text'] = 'сидит'
    b6['bg'] = '#0000ff'

    b7['text'] = 'фазан.'
    b7['bg'] = '#7d00ff'

root = Tk()

b1 = Button(text="Изменить",width=15,height=1)
b2 = Button(text="Изменить",width=15,height=1)
b3 = Button(text="Изменить",width=15,height=1)
b4 = Button(text="Изменить",width=15,height=1)
b5 = Button(text="Изменить",width=15,height=1)
b6 = Button(text="Изменить",width=15,height=1)
b7 = Button(text="Изменить",width=15,height=1)

b1.config(command=change)
b2.config(command=change)
b3.config(command=change)
b4.config(command=change)
b5.config(command=change)
b6.config(command=change)
b7.config(command=change)

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()

root.mainloop()
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

fr = Frame(root)

b1 = Button(fr,text="Изменить",width=10,height=1)
b2 = Button(fr,text="Изменить",width=10,height=1)
b3 = Button(fr,text="Изменить",width=10,height=1)
b4 = Button(fr,text="Изменить",width=10,height=1)
b5 = Button(fr,text="Изменить",width=10,height=1)
b6 = Button(fr,text="Изменить",width=10,height=1)
b7 = Button(fr,text="Изменить",width=10,height=1)

b1.config(command=change)
b2.config(command=change)
b3.config(command=change)
b4.config(command=change)
b5.config(command=change)
b6.config(command=change)
b7.config(command=change)

b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=LEFT)
b5.pack(side=LEFT)
b6.pack(side=LEFT)
b7.pack(side=LEFT)

fr.pack()

root.mainloop()
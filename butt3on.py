from tkinter import *

root = Tk()

l1 = Label(width=7,height=4,bg='yellow',text='1') 
l2 = Label(width=7,height=4,bg='red',text='0')
l3 = Label(width=7,height=4,bg='purple',text='6')
l4 = Label(width=7,height=4,bg='white',text='12')

l1.pack(side=TOP)
l2.pack(side=BOTTOM)
l3.pack(side=TOP)
l4.pack(side=BOTTOM)

root.mainloop()
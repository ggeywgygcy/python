from tkinter import *

root = Tk()

#fr_top = Frame(root)
#fr_top = Frame(root)


l1 = Label(width=7,height=4,bg='yellow',text='1') 
l2 = Label(width=7,height=4,bg='red',text='0')
l3 = Label(width=7,height=4,bg='purple',text='6')
l4 = Label(width=7,height=4,bg='white',text='12')

l1.grid(row=0,column=0)
l2.grid(row=0,column=1)
l3.grid(row=1,column=0)
l4.grid(row=1,column=1)

#fr_top.pack()
#fr_top.pack()

root.mainloop()
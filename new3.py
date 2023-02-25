from tkinter import *

root = Tk()

text = Text(width=50,height=10)
text.pack()
text.insert(1.0,'Привет мир!\nвторая строка')
text.tag_add('title',1.0,'1.end')
text.tag_config('title',justify=CENTER,font=('Arial',24,'bold'))

root.mainloop()
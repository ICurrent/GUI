from tkinter import *

root = Tk()

def my_butt(e):
    e.widgets['background'] = 'green'


but_1 = Button(root, text="Click Me")
but_1.pack()

but_1.bind("<<enter>>", my_butt)
but_1.bind("<<Leave>>", my_butt)
root.mainloop()
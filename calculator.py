from ast import Lambda, operator
from tkinter import *


root = Tk()
root.title("Calculator")
root.geometry()
#root.configure(background="sky blue")


my_input = Entry(root, width=40, borderwidth='15', bg='black', fg='white')
my_input.grid(row=0, column=0, columnspan=5)


#Get input
def button_click(number):
    num = my_input.get()
    my_input.delete(0, END)
    my_input.insert(0, str(num) + str(number))

def butt_add():
    global num_1, arith
    arith = "addition"
    num_1 = eval(my_input.get())
    my_input.delete(0, END)
    
def butt_subtract():
    global num_1, arith
    arith = "subtraction"
    num_1 = eval(my_input.get())
    my_input.delete(0, END)

def butt_multiply():
    global num_1, arith
    arith = "multiplication"
    num_1 = eval(my_input.get())
    my_input.delete(0, END)  

def butt_div():
    global num_1, arith
    arith = "division"
    num_1 = eval(my_input.get())
    my_input.delete(0, END)

def butt_equal():
    global num_2, arith
    num_2 = eval(my_input.get())
    my_input.delete(0, END)
    if arith == "addition":
        my_input.insert(0, num_1 + num_2)
    elif arith == "subtraction":
        my_input.insert(0, num_1 - num_2)
    elif arith == "multiplication":
        my_input.insert(0, num_1 * num_2)
    elif arith == "division":
        try:
            my_input.insert(0, num_1 / num_2)
        except ZeroDivisionError:
            my_input.insert(0, "ZeroDivisionError")
            #my_input.delete(0, END)
    else:
        my_input.insert(0, "Invalid operator")


def but_clear():
    my_input.delete(0, END)

button_1  = Button(root, text="1", padx=23, pady=20, font=('beauty flower', 15, 'bold'), command= lambda: button_click(1), activeforeground='white', activebackground="red")
button_2  = Button(root, text="2", padx=23, pady=20, font=('beauty flower', 15, 'bold'), command= lambda: button_click(2), activeforeground='white', activebackground="red")
button_3  = Button(root, text="3", padx=23, pady=20, font=('beauty flower', 15, 'bold'), command= lambda: button_click(3), activeforeground='white', activebackground="red")
button_4  = Button(root, text="4", padx=23, pady=20, font=('beauty flower', 15, 'bold'), command= lambda: button_click(4), activeforeground='white', activebackground="red")
button_5  = Button(root, text="5", padx=23, pady=20, font=('beauty flower', 15, 'bold'), command= lambda: button_click(5), activeforeground='white', activebackground="red")
button_6  = Button(root, text="6", padx=23, pady=20, font=('beauty flower', 15, 'bold'), command= lambda: button_click(6), activeforeground='white', activebackground="red")
button_7  = Button(root, text="7", padx=23, pady=20, font=('beauty flower', 15, 'bold'), command= lambda: button_click(7), activeforeground='white', activebackground="red")
button_8  = Button(root, text="8", padx=23, pady=20, font=('beauty flower', 15, 'bold'), command= lambda: button_click(8), activeforeground='white', activebackground="red")
button_9  = Button(root, text="9", padx=23, pady=20, font=('beauty flower', 15, 'bold'), command= lambda: button_click(9), activeforeground='white', activebackground="red")
button_0  = Button(root, text="0", padx=23, pady=20, font=('beauty flower', 15, 'bold'), command= lambda: button_click(0), activeforeground='white', activebackground="red")
button_add  = Button(root, text="+", padx=25, pady=14, font=('arial', 18, 'bold'), command= butt_add, activeforeground='white', activebackground="red")
button_substract  = Button(root, text="-", padx=25, pady=9, font=('arial', 22, 'bold'),command=butt_subtract, activeforeground='white', activebackground="red")
button_multiply  = Button(root, text="x", padx=16, pady=14, font=('arial', 18, 'bold'), command= butt_multiply, activeforeground='white', activebackground="red")
button_division  = Button(root, text="/", padx=16, pady=9, font=('arial', 22, 'bold'),command=butt_div, activeforeground='white', activebackground="red")
button_clear  = Button(root, text="clear", padx=23, pady=20, font=('beauty flower', 15, 'bold'), command= but_clear, activeforeground='white', activebackground="red")
button_equal  = Button(root, text="=", padx=25, pady=14, font=('arial', 18, 'bold'), command= butt_equal, activeforeground='white', activebackground="red")

button_0.grid(row=4, column=0)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=2, column=4)
button_substract.grid(row=3, column=4)
button_multiply.grid(row=4, column=1)
button_division.grid(row=4, column=2)
button_clear.grid(row=1, column=4)
button_equal.grid(row=4, column=4)
root.mainloop()
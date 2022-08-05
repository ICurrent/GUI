from tkinter import *
import sqlite3

base = Tk()
base.geometry("500x600")
base.title("Database")
base.config(bg="whitesmoke", highlightbackground="blue")

bg = PhotoImage(file="images.png") #Add image
canvas1 = Canvas(base, width=600, height=600) #Create canvas
canvas1.pack(expand=True, float="up")
# Display image
canvas1.create_image(0, 0, image= bg, anchor="nw")

#fill="both", expand=True

frame = Frame(base, bg="red")
#frame.pack()

def gender():
    choice = var.get()
    if choice == 1:
        output = "Male"
    elif choice == 2:
        output = "Female"
    elif choice == 3:
        output = "Not Specified"
    else:
        output = "Invalid Selection"

    return output

def checked():
    choice1 = var1.get()
    if choice1 == 0:
        choice1 = "Cereals"
    


def some_func():
    pass


label_1 = Label(base, text="His Glory Ventures", fg="white", bg="red", font=("beauty flower", 50, "bold"))
label_1.pack()

label_2 = Label(base, text="Customer Name: ", fg="black", font=("impact", 10, "italic"))
label_2.pack()
entry_1 = Entry(base, bg= "sky blue", width=50)
entry_1.pack()

label_3 = Label(base, text="E-mail Address: ", fg="black", font=("impact", 10, "italic"))
label_3.pack()
entry_2 = Entry(base, bg= "sky blue", width=50)
entry_2.pack()

label_4 = Label(base, text="Phone No: ", fg="black", font=("impact", 10, "italic"))
label_4.pack()
entry_3 = Entry(base, bg= "sky blue", width=50)
entry_3.pack()

label_5 = Label(base, text="Location: ", fg="black", font=("impact", 10, "italic"))
label_5.pack()
entry_4 = Entry(base, bg= "sky blue", width=50)
entry_4.pack()

#label_1.grid(row=0, column=2)
var = IntVar()
Label(base, text="Gender ", fg="black", font=("impact", 10, "italic")).place(x=100, y=255)
Radiobutton(base, text="Male", variable=var, value=1, command=gender).place(x=170, y=255)
Radiobutton(base, text="Female", variable=var, value=2, command=gender).place(x=230, y=255)
Radiobutton(base, text="Can't Specify", variable=var, value=3, command=gender).place(x=300, y=255)

var1 = IntVar()
Label(base, text="Products:", fg="black", font=("impact", 10, "italic")).place(x=120, y=295)
Checkbutton(base, text="Cereals", variable=var1, onvalue=0, offvalue=1, command=checked).place(x=230, y=285)
Checkbutton(base, text="Rice", variable=var1, onvalue=2, offvalue=3, command=checked).place(x=230, y=305)
Checkbutton(base, text="Garri", variable=var1, onvalue=4, offvalue=5, command=checked).place(x=230, y=325)

button = Button(base, text="Submit", relief=RAISED, font=('Arial Bold', 18))
button.place(x=200, y=350)

base.mainloop()
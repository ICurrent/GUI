import email
from tkinter import *
import sqlite3
from PIL import Image, ImageTk
from requests import delete

base = Tk()
base.geometry("500x450")
base.title("Database")
base.config(bg="whitesmoke", highlightbackground="blue")
base.resizable(False, False)
base.wm_attributes('-alpha', 0.8)
#base.attributes('-alpha', 0.7)

bg = PhotoImage(file="image/images.png") #Add image
canvas1 = Canvas(base, width=550, height=600) #Create canvas
canvas1.place(x=-60, y=0)
# Display image
canvas1.create_image(0, 0, image= bg, anchor="nw")

frame = Frame(base, bg="red")
frame.pack()


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
    choice1 = var.get()
    if choice1 == 0:
        choice1 = "Cereals"
    elif choice1 == 1:
        choice1 = "Milk"

def submit():
    #connect to database
    conn = sqlite3.connect('database/user.db')
    cursor = conn.cursor()
    # cursor.execute("""CREATE TABLE customer(
    #     name VARCHAR(30),
    #     email VARCHAR(50),
    #     phoneno VARCHAR(11),
    #     location VARCHAR(50),
    #     gender VARCHAR(30),
    #     product VARCHAR(30)
    # )

    # """) # put your sql query in the bracket

    cursor.execute("""INSERT INTO customer VALUES(:name, :email, :phoneno, :location, :gender, :product)""",
    {'name' : name.get(), 'email' : email.get(), 'phoneno' : phoneno.get(), 'location' : location.get(), 'gender' : gender.get(), 'product' : product.get()})

    # Accessing the data
    fetch = cursor.fetchall()
    for data in fetch:
        print(data)
    
    # close connection
    cursor.close()
    conn.close()


    # After submitting clear
    name.delete(0, END)
    email.delete(0, END)
    phoneno.delete(0, END)
    location.delete(0, END)



def some_func():
    pass


label_1 = Label(base, text="His Glory Ventures", fg="white", bg="red", font=("beauty flower", 50, "bold"))
label_1.pack()

label_2 = Label(base, text="Customer Name: ", fg="black", font=("impact", 10, "italic"))
label_2.pack()
name = Entry(base, bg= "sky blue", width=50)
name.pack()

label_3 = Label(base, text="E-mail Address: ", fg="black", font=("impact", 10, "italic"))
label_3.pack()
email = Entry(base, bg= "sky blue", width=50)
email.pack()

label_4 = Label(base, text="Phone No: ", fg="black", font=("impact", 10, "italic"))
label_4.pack()
phoneno = Entry(base, bg= "sky blue", width=50)
phoneno.pack()

label_5 = Label(base, text="Location: ", fg="black", font=("impact", 10, "italic"))
label_5.pack()
location = Entry(base, bg= "sky blue", width=50)
location.pack()

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

button = Button(base, text="Submit", relief=RAISED, font=('Arial Bold', 18), command=submit)
button.place(x=200, y=350)

base.mainloop()
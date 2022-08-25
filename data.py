from sre_parse import State
from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title()
root.configure(background="blue")

def submit():
    conn = sqlite3.connect("address_book.db")
    #create cursor
    c = conn.cursor()

    #insert into table
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
    {
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zipcode': zipcode.get()
    })

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

    #commit changes
    conn.commit()
    #close connection
    conn.close()

def query():
    conn = sqlite3.connect("address_book.db")
    #create cursor
    c = conn.cursor()

    c.execute('SELECT *,oid FROM addresses')
    records = c.fetchall()
    print(records)
    
    pnt_record = ""
    for i in records:
        pnt_record += str(i[6]) + ' ' + str(i[0]) + ' ' + str(i[1]) + '\n'

    query_label = Label(root, text=pnt_record)
    query_label.grid(row=10, column=0, columnspan=2)

    #commit changes
    conn.commit()
    #close connection
    conn.close()

def delete():
    conn = sqlite3.connect("address_book.db")
    #create cursor
    c = conn.cursor()

    c.execute('DELETE FROM addresses WHERE oid=' + del_box.get())
    
    del_box.delete(0, END)

    #commit changes
    conn.commit()
    #close connection
    conn.close()

def update():
    global f_name_editor, l_name_editor, address_editor
    global city_editor, state_editor, zipcode_editor
    
    conn = sqlite3.connect("address_book.db")
    #create cursor
    c = conn.cursor()

    record_id = del_box.get()
    c.execute("""
        UPDATE addresses
        SET 
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        WHERE oid = :oid""",
        {
            'first':f_name_editor,
            'last': l_name_editor,
            'address': address_editor,
            'city':city_editor,
            'state': state_editor,
            'zipcode':zipcode_editor
        })

    conn.commit()

    conn.close()

def edit():
    global f_name_editor, l_name_editor, address_editor
    global city_editor, state_editor, zipcode_editor
    
    editor = Tk()
    editor.title("Update Records")

    conn = sqlite3.connect("address_book.db")
    #create cursor
    c = conn.cursor()

    record_id = del_box.get()

    c.execute("SELECT * FROM addresses WHERE oid= " + record_id)
    records = c.fetchall()

    # pnt_record = ""
    # for i in records:
    #     pnt_record += str(i[0]) + ' ' + str(i[1]) + ' ' + '\n'

    f_name_editor = Entry(editor, width=30)
    l_name_editor = Entry(editor, width=30)
    address_editor = Entry(editor, width=30)
    city_editor = Entry(editor, width=30)
    state_editor = Entry(editor, width=30)
    zipcode_editor = Entry(editor, width=30)
    f_name_label_editor = Label(editor, text="First Name")
    l_name_label_editor = Label(editor, text="Last Name")
    address_label_editor = Label(editor, text="Address")
    city_label_editor = Label(editor, text="City")
    state_label_editor = Label(editor, text="State")
    zipcode_label_editor = Label(editor, text="Zipcode")

    f_name_editor.grid(row=0, column=1, pady=(10, 0))
    l_name_editor.grid(row=1, column=1)
    address_editor.grid(row=2, column=1)
    city_editor.grid(row=3, column=1)
    state_editor.grid(row=4, column=1)
    zipcode_editor.grid(row=5, column=1)
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
    l_name_label_editor.grid(row=1, column=0)
    address_label_editor.grid(row=2, column=0)
    city_label_editor.grid(row=3, column=0)
    state_label_editor.grid(row=4, column=0)
    zipcode_label_editor.grid(row=5, column=0)

    for record in records:
        f_name.insert(0, record[0])
        l_name.insert(0, record[1])
        address.insert(0, record[2])
        city.insert(0, record[3])
        state.insert(0, record[4])
        zipcode.insert(0, record[5])


    edit_btn = Button(editor, text="Save Record",width=18, command=update)
    edit_btn.grid(row=10, column=0, columnspan=2, pady=5, padx=10, ipadx=100)

conn = sqlite3.connect("address_book.db")

#create cursor
c = conn.cursor()

#create table
# c.execute("""CREATE TABLE addresses(
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer
# )""")

f_name = Entry(root, width=30)
l_name = Entry(root, width=30)
address = Entry(root, width=30)
city = Entry(root, width=30)
state = Entry(root, width=30)
zipcode = Entry(root, width=30)
f_name_label = Label(root, text="First Name")
l_name_label = Label(root, text="Last Name")
address_label = Label(root, text="Address")
city_label = Label(root, text="City")
state_label = Label(root, text="State")
zipcode_label = Label(root, text="Zipcode")

f_name.grid(row=0, column=1, pady=(10, 0))
l_name.grid(row=1, column=1)
address.grid(row=2, column=1)
city.grid(row=3, column=1)
state.grid(row=4, column=1)
zipcode.grid(row=5, column=1)
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label.grid(row=1, column=0)
address_label.grid(row=2, column=0)
city_label.grid(row=3, column=0)
state_label.grid(row=4, column=0)
zipcode_label.grid(row=5, column=0)

sunmit_btn = Button(root, text="Add Record to Database", command=submit)
sunmit_btn.grid(row=6, column=0, columnspan=2, pady=5, padx=6, ipadx=100)

#create a query button
query_btn = Button(root, text="Show Records", width=10, command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=3, padx=10, ipadx=130)

sel_label = Label(root, text="Selete ID")
sel_label.grid(row=8, column=0)

del_box = Entry(root, width=30)
del_box.grid(row=8, column=1)

del_btn = Button(root, text="Delete", width=18, command=delete)
del_btn.grid(row=9, column=0, columnspan=2, pady=5, padx=10, ipadx=100)

edit_btn = Button(root, text="Edit Record",width=18, command=edit)
edit_btn.grid(row=10, column=0, columnspan=2, pady=5, padx=10, ipadx=100)

#commit changes
conn.commit()
#close connection
conn.close()

root.mainloop()
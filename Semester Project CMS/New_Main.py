

import tkinter
from tkinter import *
from functools import partial

import os






# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Backend database connection:

import pyodbc

connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + os.path.join('Database', 'db.accdb') +';')
cursor = connection.cursor()

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Helper Functions:

# This function adds new record to database:
def create_record(name, phone, description):
    cursor.execute('INSERT INTO contacts (name, phone, description) VALUES (\''+name.get()+'\', \''+phone.get()+'\', \''+description.get()+'\');')
    cursor.commit()

def get_all_records():
    cursor.execute('select * from contacts')
    return cursor.fetchall()

def delete(pk):
    cursor.execute('DELETE FROM contacts WHERE ID=' + pk.get())
    cursor.commit()

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::







def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
root = Tk()
root.geometry('256x600')
root.title('Contact Management System')
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Login", command=donothing)
filemenu.add_command(label="Signup", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="User", menu=filemenu)

"""
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edt", menu=editmenu)
"""
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)



#####################################################################
"""
canvas = Canvas(root, width = 300, height = 300)          
photo = PhotoImage(file = os.path.join('Assets', 'book.jpg'))     
canvas.create_image(20,20, anchor=NW, image=photo)
canvas.pack()
"""

frame = Frame(root)
frame.pack()
#####################################################################
# Register Data:

register_label = Label(frame, text="Register New Student", font="bold").pack()

# Get 'Name' fro User and store in name variable
name_label = Label(frame, text="Name").pack()
name = StringVar()
name_entry = Entry(frame, textvariable=name).pack()

# Get 'Phone Number' from user in store in phone variable
phone_label = Label(frame,text="Phone no.").pack()
phone = StringVar()
phone_entry = Entry(frame, textvariable=phone).pack()

# Get 'Description' from user in store in description variable
description_label = Label(frame,text="Description").pack()
description = StringVar()
description_entry = Entry(frame, textvariable=description).pack()

create = partial(create_record, name, phone, description)

# Create new entry button
create_new_button = Button(frame, text="Create", fg="blue", command=create).pack()


#####################################################################



root.mainloop()

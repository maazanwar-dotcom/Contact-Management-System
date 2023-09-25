
# ::::::::::::::::::::: Contact Management System ::::::::::::::::::::::

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Authors:
# Muhmmad Mujtaba SP22-BSE-036 1A
# Maaz Anwar SP22-BSE- 1A
# Eman Basharat SP22-BSE- 1A
# Khola Gohar SP22-BSE- 1A

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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

# Window:

tkWindow = Tk()
tkWindow.geometry('256x600')
tkWindow.title('Contact Management System')

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Register Data:

register_label = Label(tkWindow, text="Create New Contact").grid(row=0, column=1)

# Get 'Name' fro User and store in name variable
name_label = Label(tkWindow, text="Name").grid(row=1, column=0)
name = StringVar()
name_entry = Entry(tkWindow, textvariable=name).grid(row=1, column=1)

# Get 'Phone Number' from user in store in phone variable
phone_label = Label(tkWindow,text="Phone no.").grid(row=2, column=0)
phone = StringVar()
phone_entry = Entry(tkWindow, textvariable=phone).grid(row=2, column=1)

# Get 'Description' from user in store in description variable
description_label = Label(tkWindow,text="Description").grid(row=3, column=0)
description = StringVar()
description_entry = Entry(tkWindow, textvariable=description).grid(row=3, column=1)

create = partial(create_record, name, phone, description)

# Create new entry button
create_new_button = Button(tkWindow, text="Create", command=create).grid(row=5, column=1)

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Delete Data:

delete_label = Label(tkWindow, text="Delete Contact").grid(row=6, column=1)

# Get 'Description' from user in store in description variable
pk_label = Label(tkWindow,text="Primary Key").grid(row=7, column=0)
pk = StringVar()
pk_entry = Entry(tkWindow, textvariable=pk).grid(row=7, column=1)

delete = partial(delete, pk)

# Create new entry button
delete_button = Button(tkWindow, text="Delete", command=delete).grid(row=8, column=1)

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Retrive Data:

tiny_window = Toplevel()
tiny_window.geometry('256x512')
contacts_list_label = Label(tiny_window, text = "Contacts List")
contacts_list_label.pack()
for record in get_all_records():
    separaton_line = Label(tiny_window, text = '--------------------------')
    contact_id = Label(tiny_window, text = 'ID: '+str(record.ID))
    contact_name = Label(tiny_window, text = ' Name: '+str(record.name))
    contact_phone = Label(tiny_window, text = ' Phone no.: '+str(record.phone))
    contact_description = Label(tiny_window, text = ' Description: '+str(record.description))
    separaton_line.pack()
    contact_id.pack()
    contact_name.pack()
    contact_phone.pack()
    contact_description.pack()

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

tkWindow.mainloop()

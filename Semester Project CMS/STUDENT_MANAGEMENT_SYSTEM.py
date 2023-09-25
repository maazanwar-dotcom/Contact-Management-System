
import os
import time

import pyodbc

title = """
███████╗████████╗██╗   ██╗██████╗ ███████╗███╗   ██╗████████╗
██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝████╗  ██║╚══██╔══╝
███████╗   ██║   ██║   ██║██║  ██║█████╗  ██╔██╗ ██║   ██║   
╚════██║   ██║   ██║   ██║██║  ██║██╔══╝  ██║╚██╗██║   ██║   
███████║   ██║   ╚██████╔╝██████╔╝███████╗██║ ╚████║   ██║   
╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   
                                                                     
                                              
     █▀▄▀█ ▄▀█ █▄░█ ▄▀█ █▀▀ █▀▀ █▀▄▀█ █▀▀ █▄░█ ▀█▀
     █░▀░█ █▀█ █░▀█ █▀█ █▄█ ██▄ █░▀░█ ██▄ █░▀█ ░█░

                             
               █▀ █▄█ █▀ ▀█▀ █▀▀ █▀▄▀█
               ▄█ ░█░ ▄█ ░█░ ██▄ █░▀░█

   
 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

"""

menu = """
                   
                █▀▄▀█ █▀▀ █▄░█ █░█
                █░▀░█ ██▄ █░▀█ █▄█

               * * * * * * * * * **
               *                  *
               * Register Student * -> 1
               *                  *
               *                  *
               *   Login Student  * -> 2
               *                  *
               *                  *
               *  Student's List  * -> 3
               *                  *
               *                  *
               *       Exit       * -> 0
               *                  *
               *                  *
               ** * * * * * * * * *
"""

register_choices = """
               * * * * * * * * * **
               *                  *
               *     Continue     * -> 1
               *                  *
               *       Back       * -> 0
               *                  *
               ** * * * * * * * * *
"""

students_list_choices = """
               * * * * * * * * * **
               *                  *
               *  Student's Info  * -> ROLL NO.
               *                  *
               *       Back       * -> 0
               *                  *
               ** * * * * * * * * *
"""

_list = """
             
 █░░ █ █▀ ▀█▀
 █▄▄ █ ▄█ ░█░

"""

back = """
               * * * * * * * * * **
               *                  *
               *       Back       * -> 0
               *                  *
               ** * * * * * * * * *
"""

info = """
               
 █ █▄░█ █▀▀ █▀█
 █ █░▀█ █▀░ █▄█

"""

connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + os.path.join('Database', 'db.accdb') +';')
cursor = connection.cursor()


# This function adds new record to database:
def create_record(name, phone, description):
    cursor.execute('INSERT INTO user (name, phone, description) VALUES (\''+name+'\', \''+phone+'\', \''+description+'\');')
    cursor.commit()

def get_all_records():
    cursor.execute('select * from user')
    return cursor.fetchall()

def delete(ID):
    cursor.execute('DELETE FROM user WHERE ID=' + ID)
    cursor.commit()


def display_student_info(ID):
    os.system('cls')
    print(title)
    for record in get_all_records():
        if ID in record:
            print(info)
            print("Name: ", record.name)
            print("Roll no.: ", record.ID)
            print("Phone: ", record.phone)
            print("Description: ", record.description)
    z = input("Press Enter to Go Back")

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def display_students_list():
    os.system('cls')
    print(title)
    print(students_list_choices)
    print(_list)
    for record in get_all_records():
        print("Roll no. " + str(record.ID) + ", Name: " + record.name + ", Phone: " + record.phone)
        
    choice = int(input("Enter your choice: "))
    if choice == 0: return
    else:
        display_student_info(choice)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def register_student():
    os.system('cls')
    print(title)

    password = input("Enter Admin Password: ")
    if password != "admin":
        print("You must be an admin to perform this operation!")
        time.sleep(3)
        return
    print(register_choices)
    choice = int(input("Are you sure you want to continue? "))
    if choice == 1:
        name = input("Enter Student's Name: ")
        phone = input("Enter Student's Phone: ")
        description = input("Enter Student's Description: ")
        create_record(name, phone, description)
    elif choice == 0: return

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def login_student():
    os.system('cls')
    print(title)

    key = int(input("Enter Student Roll Number: "))
    for record in get_all_records():
        if key in record:
            display_student_info(key)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def main_menu():
    os.system('cls')
    print(title)
    
    print(menu)
    choice = int(input("Enter your choice: "))
    if   choice == 1: register_student()
    elif choice == 2: login_student()
    elif choice == 3:
        key = input("Enter Admin Key: ")
        if key != "admin": return
        display_students_list()
    elif choice == 0: exit()

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def main():
    while True:
        main_menu()










main()

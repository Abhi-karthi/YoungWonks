from getpass import getpass
# from tkinter import *
import sqlite3
import random
import time

# root = Tk()
# root.size("512x288")
# main_menu_frame = Frame(root)
# login_page_frame = Frame(root)
# signup_page_frame = Frame(root)
# dashboard_page_frame = Frame(root)
# hack_page_frame = Frame(root)
# root.title("LOGIN WITH SQLITE")

conn = sqlite3.connect("login_database.db")
c = conn.cursor()
current_login_value = []

# try:
#     c.execute('CREATE TABLE login_info (name TEXT, username TEXT, password TEXT, data TEXT)')
# except sqlite3.OperationalError:
#     pass


def save():
    global conn
    global c
    conn.commit()
    conn.rollback()
    c.close()
    conn.close()
    conn = sqlite3.connect("login_database.db")
    c = conn.cursor()

def next_page():
    time.sleep(0.5)
    for i in range(23):
        print()


def hack_screen():
    characters = list("`1290-=qop[]\sjkl;'zxcvbnm,./~!@#$%^&*()_+QWIOP{}|ASKL:ZM<>`¡™£¢∞§¶•ªº–≠?«åß∂ƒ©˙∆˚¬…æΩç√∫˜µ")
    for i in range(45):
        for x in range(125):
            print(random.choice(characters), end="")
            time.sleep(0.000125)
        print()
    print()


def main_menu():
    print("MAIN MENU")
    print("1. SIGNUP")
    print("2. LOGIN")
    print("3. EXIT")
    print("ENTER YOUR CHOICE (1/2/3): ", end="")
    accept = 0
    operation_var = "var"
    choice = 0
    while accept == 0:
        try:
            choice = int(input())
            if choice == 1 or choice == 2 or choice == 3 or choice == 3141592653589:
                next_page()
                accept = 1
            else:
                operation_var = int(operation_var)
        except ValueError:
            print()
            print("PLEASE ENTER A NUMBER (1, 2, OR 3).")
            print("ENTER YOUR CHOICE (1/2/3): ", end="")

    if choice == 1:
        signup_page()
    elif choice == 2:
        login_page()
    elif choice == 3:
        conn.commit()
        conn.rollback()
        c.close()
        conn.close()
        print("SUCCESSFULLY EXITED")
        exit()
    elif choice == 3141592653589:
        hack_screen()
        next_page()
        print("HACK MENU")
        print("1. SEE ALL LOGIN INFO AND DATA")
        print("2. DELETE EVERYTHING")
        print("3. EXIT")
        print("ENTER YOUR CHOICE (1/2/3): ", end="")
        accept = 0
        operation_var = "var"
        choice = 0
        while accept == 0:
            try:
                choice = int(input())
                if choice == 1 or choice == 2 or choice == 3:
                    next_page()
                    accept = 1
                else:
                    operation_var = int(operation_var)
            except ValueError:
                print()
                print("PLEASE ENTER A NUMBER (1, 2, OR 3).")
                print("ENTER YOUR CHOICE (1/2/3): ", end="")

        if choice == 1:
            hack_screen()
            next_page()
            c.execute('SELECT * FROM login_info')
            check_if_empty = False

            for r in c:
                print(f"{r[0]}|{r[1]}|{r[2]}|{r[3]}")
                check_if_empty = True

            if not check_if_empty:
                print("NO LOGIN INFO OR DATA DETECTED")
                print()

            input("ENTER ANYTHING WHEN FINISHED: ")
            hack_screen()
            next_page()
            main_menu()
        elif choice == 2:
            c.execute('DROP TABLE login_info')
            input("DATA TERMINATED SUCCESSFULLY. ENTER ANYTHING TO EXIT: ")
            hack_screen()
            next_page()
            main_menu()
        elif choice == 3:
            hack_screen()
            next_page()
            print("SUCCESSFULLY ENDED HACK SESSION")
            next_page()
            main_menu()


def login_page():
    global current_login_value
    print("LOGIN PAGE")
    print("USERNAME: ", end="")
    username_input = input()
    print()
    password_input = getpass("PASSWORD: ")
    print()
    success = False
    c.execute('SELECT * FROM login_info')
    for r in c:
        if str(r[1]).lower() == username_input.lower() and r[2] == password_input:
            current_login_value = [r[0], username_input, password_input]
            success = True


    if success:
        print("LOGIN SUCCESSFUL")
        next_page()
        dashboard_page()
    else:
        print("INCORRECT")
        next_page()
        main_menu()


def signup_page():
    global current_login_value
    print("SIGNUP PAGE")
    print("ENTER YOUR NAME: ", end='')
    name_value = input()
    print()
    print('ENTER YOUR USERNAME: ', end='')
    username_value = str(input())
    c.execute('SELECT username FROM login_info')
    for r in c:
        if username_value.lower() == str(r[0]).lower():
            print("YOU HAVE THE SAME USERNAME AS SOMEONE ELSE. PLEASE TRY AGAIN.")
            next_page()
            main_menu()
    print()
    password_value = getpass('ENTER YOUR SECURE PASSWORD WITH AT LEAST ONE DIGIT AND ONE CAPITAL LETTER: ')
    print()
    password_value2 = getpass('ENTER YOUR PASSWORD AGAIN: ')
    print()
    # print('ENTER YOUR DATA: ', end='')
    # data_value = input()
    if password_value == password_value2:
        valid_digit = False
        valid_digits = list("1234567890")
        valid_capital = False
        valid_capitals = list("QWERTYUIOPASDFGHJKLZXCVBNM")
        for i in password_value:
            if i in valid_digits:
                valid_digit = True
            if i in valid_capitals:
                valid_capital = True

        if valid_digit and valid_capital:
            c.execute('INSERT INTO login_info (name, username, password, data) VALUES (?, ?, ?, ?)', (name_value, username_value, password_value, ""))
            print('LOGIN SUCCESSFUL')
            current_login_value = [name_value, username_value, password_value]
            save()
            next_page()
            dashboard_page()
        else:
            print("LOGIN UNSUCCESSFUL: PASSWORD ISN'T SECURE ENOUGH. PLEASE TRY AGAIN.")
            next_page()
            signup_page()
    else:
        print("LOGIN UNSUCCESSFUL: PASSWORDS DIDN'T MATCH. PLEASE TRY AGAIN.")
        next_page()
        signup_page()



def dashboard_page():
    global current_login_value
    print("DASHBOARD MENU")
    print(f"HELLO, {current_login_value[0].upper()}.")
    print("1. CHANGE PASSWORD")
    print("2. ADD/CHANGE DATA")
    print("3. SEE DATA")
    print("4. EXIT")
    response = 0

    try:
        response = int(input("ENTER YOUR CHOICE (1/2/3/4): "))
        if not (response == 1 or response == 2 or response == 3 or response == 4):
            print("PLEASE ENTER A NUMERICAL VALUE (1, 2, 3, OR 4).")
            next_page()
            dashboard_page()
        else:
            next_page()
    except ValueError:
        print("PLEASE ENTER A NUMERICAL VALUE (1, 2, 3, OR 4).")
        next_page()
        dashboard_page()

    if response == 1:
        curr_password = getpass("ENTER CURRENT PASSWORD: ")
        if curr_password == current_login_value[2]:
            new_password = getpass("ENTER YOUR NEW PASSWORD: ")
            new_password_conformation = getpass("ENTER YOUR NEW PASSWORD AGAIN: ")
            if new_password == new_password_conformation:
                valid_digit = False
                valid_digits = list("1234567890")
                valid_capital = False
                valid_capitals = list("QWERTYUIOPASDFGHJKLZXCVBNM")
                for i in new_password:
                    if i in valid_digits:
                        valid_digit = True
                    if i in valid_capitals:
                        valid_capital = True

                if valid_digit and valid_capital:
                    c.execute("UPDATE login_info SET password=? WHERE password=?",(new_password, current_login_value[2]))
                    current_login_value[2] = new_password
                    print("PASSWORD UPDATED SUCCESSFULLY.")
                    save()
                    next_page()
                    dashboard_page()
                else:
                    print("LOGIN UNSUCCESSFUL: PASSWORD ISN'T SECURE ENOUGH. PLEASE TRY AGAIN.")
                    next_page()
                    dashboard_page()

            else:
                print("PASSWORDS DON'T MATCH. PLEASE TRY AGAIN.")
                next_page()
                dashboard_page()
        else:
            print("INCORRECT PASSWORD. PLEASE TRY AGAIN.")
            next_page()
            dashboard_page()
    elif response == 2:
        new_data = input("ENTER YOUR NEW DATA: ")
        c.execute("UPDATE login_info SET data=? WHERE username=?", (new_data, current_login_value[1]))
        print("DATA UPDATED SUCCESSFULLY.")
        save()
        next_page()
        dashboard_page()
    elif response == 3:
        c.execute('SELECT data FROM login_info WHERE username=? AND password=?', (current_login_value[1], current_login_value[2]))
        print("DATA RETRIEVED SUCCESSFULLY:")
        for r in c:
            print(r[0])
        input("ENTER ANYTHING WHEN DONE: ")
        next_page()
        dashboard_page()
    elif response == 4:
        save()
        current_login_value = []
        print("EXITING...")
        next_page()
        main_menu()


next_page()
main_menu()

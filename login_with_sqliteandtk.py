from tkinter import *
import sqlite3
import time

from Cython.Utils import open_source_from_loader

root = Tk()
root.geometry("608x342")
main_menu_frame = Frame(root)
login_page_frame = Frame(root)
signup_page_frame = Frame(root)
dashboard_page_frame = Frame(root)
change_password_frame = Frame(root)
see_data_frame = Frame(root)
change_data_frame = Frame(root)
hack_page_frame = Frame(root)
main_menu_frame.pack()
root.title("LOGIN WITH SQLITE")

# root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(0, weight=1)

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


def signup_button_for_main_menu_frame_command():
    main_menu_frame.pack_forget()
    signup_page_frame.pack()


def login_button_for_main_menu_frame_command():
    main_menu_frame.pack_forget()
    login_page_frame.pack()


def exit_button_for_main_menu_frame_command():
    save()
    exit()


checked_timer = time.time()
cap_letters_list = list("QWERTYUIOPASDFGHJKLZXCVBNM")
nums_list = list("1234567890")
# Main Menu
main_label_for_main_menu = Label(main_menu_frame, text="MAIN MENU:", font=("Arial", 52))
signup_button_for_main_menu = Button(main_menu_frame, text="SIGN UP", command=signup_button_for_main_menu_frame_command, font=("Arial", 40))
login_button_for_main_menu = Button(main_menu_frame, text="LOGIN", command=login_button_for_main_menu_frame_command, font=("Arial", 40))
exit_button_for_main_menu = Button(main_menu_frame, text="EXIT", command=exit_button_for_main_menu_frame_command, font=("Arial", 40))

main_label_for_main_menu.grid(row=0, column=0)
signup_button_for_main_menu.grid(row=1, column=0)
login_button_for_main_menu.grid(row=2, column=0)
exit_button_for_main_menu.grid(row=3, column=0)


# Sign Up Page
username_success = True
password_repeat_success = False
password_security_success = False
signup_success = False
checked = False
current_bad_username = ""
current_good_password = ""
main_label_for_signup_page = Label(signup_page_frame, text="SIGN UP PAGE", font=("Arial", 40))

name_label_for_signup_page = Label(signup_page_frame, text="NAME: ", font=("Arial", 29))
name_entry_for_signup_page = Entry(signup_page_frame)

username_label_for_signup_page = Label(signup_page_frame, text="USERNAME: ", font=("Arial", 29))
username_entry_for_signup_page = Entry(signup_page_frame)

username_entry_for_signup_page_feedback_variable = StringVar()
username_entry_for_signup_page_feedback = Label(signup_page_frame, textvariable=username_entry_for_signup_page_feedback_variable, font=("Arial", 8))
username_entry_for_signup_page_feedback_variable.set("")

password_label_for_signup_page = Label(signup_page_frame, text="PASSWORD: ", font=("Arial", 29))
password_entry_for_signup_page = Entry(signup_page_frame, show="*")
repassword_label_for_signup_page = Label(signup_page_frame, text="REENTER PASSWORD: ", font=("Arial", 29))
repassword_entry_for_signup_page = Entry(signup_page_frame, show="*")

password_entry_for_signup_page_feedback_variable = StringVar()
password_entry_for_signup_page_feedback = Label(signup_page_frame, textvariable=password_entry_for_signup_page_feedback_variable, font=("Arial", 8))
repassword_entry_for_signup_page_feedback_variable = StringVar()
repassword_entry_for_signup_page_feedback = Label(signup_page_frame, textvariable=repassword_entry_for_signup_page_feedback_variable, font=("Arial", 8))

def check_entries():
    global signup_success
    global name_entry_for_signup_page
    global username_entry_for_signup_page
    global password_entry_for_signup_page
    global current_login_value
    global current_bad_username
    global password_entry_for_signup_page_feedback
    global username_success
    global password_repeat_success
    global cap_letters_list_in
    global nums_list_in
    global password_security_success
    username_success = True
    c.execute("SELECT username FROM login_info")
    # username_success = True (Declared above)
    for r in c:
        # print(r[0], username_entry_for_signup_page.get(), 1)
        if r[0].lower() == username_entry_for_signup_page.get().lower():
            username_entry_for_signup_page_feedback_variable.set("THIS USERNAME IS TAKEN. PLEASE ENTER A NEW ONE.")
            current_bad_username = username_entry_for_signup_page.get()
            username_success = False

    if username_success:
        username_entry_for_signup_page_feedback_variable.set("")

    if password_entry_for_signup_page.get() == repassword_entry_for_signup_page.get():
        repassword_entry_for_signup_page_feedback_variable.set("")
        password_repeat_success = True
    else:
        repassword_entry_for_signup_page_feedback_variable.set("PASSWORDS ARE NOT MATCHING")
        password_repeat_success = False

    cap_letters_list_in = False
    nums_list_in = False
    password_entry_for_signup_page_feedback_variable.set("PASSWORD IS NOT SECURE ENOUGH: MUST HAVE ONE CAPITAL AND ONE NUMERICAL CHARACTER.") # fix flickering
    for i in password_entry_for_signup_page.get():
        if i in cap_letters_list:
            cap_letters_list_in = True
            # current_good_password = password_entry_for_signup_page.get()
        elif i in nums_list:
            nums_list_in = True
            # current_good_password = password_entry_for_signup_page.get()

    if cap_letters_list_in and nums_list_in:
        password_entry_for_signup_page_feedback_variable.set("")
        password_security_success = True
    elif cap_letters_list_in == True and nums_list_in == False:
        password_entry_for_signup_page_feedback_variable.set("PASSWORD IS NOT SECURE ENOUGH: MUST HAVE AT LEAST ONE NUMBER")
    elif cap_letters_list_in == False and nums_list_in == True:
        password_entry_for_signup_page_feedback_variable.set("PASSWORD IS NOT SECURE ENOUGH: MUST HAVE AT LEAST ONE CAPITAL LETTER")

    if password_security_success and password_repeat_success and username_success:
        signup_success = True

    root.after(10, check_entries)

root.after(0, check_entries)

def signup_button_command():
    global signup_success
    global name_entry_for_signup_page
    global username_entry_for_signup_page
    global password_entry_for_signup_page
    global current_login_value
    global current_bad_username
    global password_entry_for_signup_page_feedback
    global username_success
    global password_repeat_success
    global cap_letters_list_in
    global nums_list_in
    global password_security_success

    c.execute("SELECT username FROM login_info")
    username_success = True
    for r in c:
        if r[0].lower() == username_entry_for_signup_page.get().lower():
            username_entry_for_signup_page_feedback_variable.set("THIS USERNAME IS TAKEN. PLEASE ENTER A NEW ONE.")
            # current_bad_username = username_entry_for_signup_page.get()
            username_success = False

    if username_success:
        username_entry_for_signup_page_feedback_variable.set("")


    if password_entry_for_signup_page.get() == repassword_entry_for_signup_page.get():
        repassword_entry_for_signup_page_feedback_variable.set("")
        password_repeat_success = True
    else:
        repassword_entry_for_signup_page_feedback_variable.set("PASSWORDS ARE NOT MATCHING")
        password_repeat_success = False

    cap_letters_list_in = False
    nums_list_in = False
    password_entry_for_signup_page_feedback_variable.set("PASSWORD IS NOT SECURE ENOUGH: MUST HAVE ONE CAPITAL AND ONE NUMERICAL CHARACTER.")  # fix flickering
    for i in password_entry_for_signup_page.get():
        if i in cap_letters_list:
            cap_letters_list_in = True
        elif i in nums_list:
            nums_list_in = True

    if cap_letters_list_in and nums_list_in:
        password_entry_for_signup_page_feedback_variable.set("")
        password_security_success = True
    elif cap_letters_list_in == True and nums_list_in == False:
        password_entry_for_signup_page_feedback_variable.set("PASSWORD IS NOT SECURE ENOUGH: MUST HAVE AT LEAST ONE NUMBER")
    elif cap_letters_list_in == False and nums_list_in == True:
        password_entry_for_signup_page_feedback_variable.set("PASSWORD IS NOT SECURE ENOUGH: MUST HAVE AT LEAST ONE CAPITAL LETTER")

    if password_security_success and password_repeat_success and username_success:
        signup_success = True


    if signup_success:
            c.execute("INSERT INTO login_info (name, username, password) VALUES (?, ?, ?)", (name_entry_for_signup_page.get(), username_entry_for_signup_page.get(), password_entry_for_signup_page.get()))
            current_login_value = [name_entry_for_signup_page.get(), username_entry_for_signup_page.get(), password_entry_for_signup_page.get()]
            name_entry_for_signup_page.delete(0, END)
            username_entry_for_signup_page.delete(0, END)
            password_entry_for_signup_page.delete(0, END)
            repassword_entry_for_signup_page.delete(0, END)
            save()
            dashboard_page_frame.pack()
            signup_page_frame.pack_forget()


def back_button_signup_command():
    name_entry_for_signup_page.delete(0, END)
    username_entry_for_signup_page.delete(0, END)
    password_entry_for_signup_page.delete(0, END)
    repassword_entry_for_signup_page.delete(0, END)
    signup_page_frame.pack_forget()
    main_menu_frame.pack()


signup_button = Button(signup_page_frame, text="SIGN UP", font=("Arial", 39), command=signup_button_command)
back_button_signup = Button(signup_page_frame, text="BACK", font=("Arial", 25), command=back_button_signup_command)

main_label_for_signup_page.grid(row=0, column=0) #, sticky="nsew")
name_label_for_signup_page.grid(row=1, column=0)
name_entry_for_signup_page.grid(row=1, column=1)
username_label_for_signup_page.grid(row=2, column=0)
username_entry_for_signup_page.grid(row=2, column=1)
username_entry_for_signup_page_feedback.grid(row=3, column=0) #, sticky="nsew")
password_label_for_signup_page.grid(row=4, column=0)
password_entry_for_signup_page.grid(row=4, column=1)
password_entry_for_signup_page_feedback.grid(row=5, column=0) #, sticky="nsew")
repassword_label_for_signup_page.grid(row=6, column=0)
repassword_entry_for_signup_page.grid(row=6, column=1)
repassword_entry_for_signup_page_feedback.grid(row=7, column=0) #, sticky="nsew")
signup_button.grid(row=8, column=0) # , sticky="nsew")
back_button_signup.grid(row=8, column=1)


# Login Page
main_label_for_login_page = Label(login_page_frame, text="LOGIN MENU: ", font=("Arial", 52))
username_label_for_login_page = Label(login_page_frame, text="USERNAME: ", font=("Arial", 39))
username_entry_for_login_page = Entry(login_page_frame)
password_label_for_login_page = Label(login_page_frame, text="PASSWORD: ", font=("Arial", 39))
password_entry_for_login_page = Entry(login_page_frame, show="*")
password_label_feedback_login_page_var = StringVar()
password_label_feedback_login_page = Label(login_page_frame, textvariable=password_label_feedback_login_page_var, font=("Arial", 8))


def login_button_command():
    global username_entry_for_login_page
    global password_entry_for_login_page
    global current_login_value
    c.execute('SELECT * FROM login_info')
    success = False
    for r in c:
        if r[1] == username_entry_for_login_page.get() and r[2] == password_entry_for_login_page.get():
            success = True
            current_login_value = [r[0], r[1], r[2]]

    if success:
        username_entry_for_login_page.delete(0, END)
        password_entry_for_login_page.delete(0, END)
        password_label_feedback_login_page_var.set("s")
        login_page_frame.pack_forget()
        dashboard_page_frame.pack()
    else:
        password_entry_for_login_page.delete(0, END)
        password_label_feedback_login_page_var.set("USERNAME OR PASSWORD IS INCORRECT")


def back_button_login_command():
    global current_login_value

    current_login_value = []
    username_entry_for_login_page.delete(0, END)
    password_entry_for_login_page.delete(0, END)
    password_label_feedback_login_page_var.set("")
    login_page_frame.pack_forget()
    main_menu_frame.pack()


login_button = Button(login_page_frame, text="LOGIN", font=("Arial", 39), command=login_button_command)
back_button_login = Button(login_page_frame, text="BACK", font=("Arial", 39), command=back_button_login_command)

main_label_for_login_page.grid(row=0, column=0)
username_label_for_login_page.grid(row=1, column=0)
username_entry_for_login_page.grid(row=1, column=1)
password_label_for_login_page.grid(row=2, column=0)
password_entry_for_login_page.grid(row=2, column=1)
password_label_feedback_login_page.grid(row=3, column=0)
login_button.grid(row=4, column=0)
back_button_login.grid(row=4, column=1)


# Dashboard Page


def change_password_button_command():
    dashboard_page_frame.pack_forget()
    change_password_frame.pack()


def see_data_button_command():
    dashboard_page_frame.pack_forget()
    see_data_frame.pack()


def change_data_button_command():
    dashboard_page_frame.pack_forget()
    change_password_frame.pack()


def exit_dashboard_button_command():
    global current_login_value

    current_login_value = []
    save()
    dashboard_page_frame.pack_forget()
    main_menu_frame.pack()


main_label_for_dashboard_page = Label(dashboard_page_frame, text="DASHBOARD", font=("Arial", 20))
if len(current_login_value) > 0:
    introduction_for_dashboard_page = Label(dashboard_page_frame, text=f"HELLO, {current_login_value[0].upper()}.")
else:
    introduction_for_dashboard_page = Label(dashboard_page_frame, text="HELLO")
change_password_button = Button(dashboard_page_frame, text="CHANGE PASSWORD", command=change_password_button_command, font=("Arial", 40))
see_data_button = Button(dashboard_page_frame, text="SEE DATA", command=see_data_button_command, font=("Arial", 40))
change_data_button = Button(dashboard_page_frame, text="CHANGE DATA", command=change_data_button_command, font=("Arial", 40))
exit_dashboard_button = Button(dashboard_page_frame, text="EXIT DASHBOARD", command=exit_dashboard_button_command, font=("Arial", 40))

main_label_for_dashboard_page.grid(row=0, column=0)
introduction_for_dashboard_page.grid(row=1, column=0)
change_password_button.grid(row=2, column=0)
see_data_button.grid(row=3, column=0)
change_data_button.grid(row=4, column=0)
exit_dashboard_button.grid(row=5, column=0)


# Change Password Page
main_label_change_password_page = Label(change_password_frame, text="CHANGE PASSWORD", font=("Arial", 52))
old_password_label = Label(change_password_frame, text="ENTER YOUR OLD PASSWORD", font=("Arial", 39))
old_password_entry = Entry(change_password_frame, show="*")
old_password_feedback_variable = StringVar()
old_password_feedback_label = Label(change_password_frame, textvariable=old_password_feedback_variable, font=("Arial", 8))
new_password_label = Label(change_password_frame, text="ENTER YOUR NEW PASSWORD", font=("Arial", 39))
new_password_entry = Entry(change_password_frame, show="*")
new_password_feedback_variable = StringVar()
new_password_feedback_label = Label(change_password_frame, textvariable=new_password_feedback_variable, font=("Arial", 6))
new_repassword_label = Label(change_password_frame, text="ENTER YOUR NEW PASSWORD AGAIN", font=("Arial", 39))
new_repassword_entry = Entry(change_password_frame, show="*")
new_repassword_feedback_variable = StringVar()
new_repassword_feedback_label = Label(change_password_frame, textvariable=new_repassword_feedback_variable, font=("Arial", 6))


def change_password_button_command():
    global current_login_value
    global old_password_feedback_variable
    global new_password_feedback_variable
    global new_repassword_feedback_variable
    global cap_letters_list
    global nums_list

    # change_password_valid = False
    nonrepeating_password = False
    cap_in = False
    nums_in = False
    old_password_correct = False

    if old_password_feedback_variable.get() == current_login_value[2]:
        old_password_correct = True
        old_password_feedback_variable.set("")
    else:
        old_password_feedback_variable.set("PASSWORD INCORRECT")

    for i in new_password_feedback_variable.get():
        if i in cap_letters_list:
            cap_in = True
        elif i in nums_list:
            nums_in = True

    if cap_in and nums_in:
        old_password_feedback_variable.set("")
    elif cap_in and (not nums_in):
        old_password_feedback_variable.set("PASSWORD MUST HAVE AT LEAST ONE NUMBER")
    elif nums_in and (not cap_in):
        old_password_feedback_variable.set("PASSWORD MUST HAVE AT LEAST ONE CAPITAL LETTER")
    elif not (nums_in or cap_in):
        old_password_feedback_variable.set("PASSWORD MUST HAVE AT LEAST ONE CAPITAL LETTER AND ONE NUMBER")

    if new_password_feedback_variable == new_repassword_feedback_variable:
        nonrepeating_password = True
        new_repassword_feedback_variable.set("")
    else:
        new_repassword_feedback_variable.set("PASSWORDS DON'T MATCH")

    if nonrepeating_password and cap_in and nums_in and old_password_correct:
        c.execute("UPDATE login_info SET password=? WHERE password=?",(new_password_entry.get(), current_login_value[2]))
        save()
        current_login_value[2] = new_password_entry.get()
        old_password_entry.delete(0, END)
        new_password_entry.delete(0, END)
        new_repassword_entry.delete(0, END)
        change_password_frame.pack_forget()
        dashboard_page_frame.pack()


def back_button_change_password_command():
    old_password_entry.delete(0, END)
    new_password_entry.delete(0, END)
    new_repassword_entry.delete(0, END)
    old_password_feedback_variable.set("")
    new_repassword_feedback_variable.set("")




root.mainloop()

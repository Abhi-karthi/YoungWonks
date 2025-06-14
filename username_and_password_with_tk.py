from tkinter import *
from tkinter import messagebox
import time
root = Tk()
root.title("Username and Password")
username_label = Label(root, text="Username:")
pass_label = Label(root, text="Password:")
username_entry = Entry(root)
pass_entry = Entry(root, show="*")
regex_variable = IntVar()
match_variable = IntVar()
check_regular_expression = Checkbutton(root, text='Regular expression', variable=regex_variable)
check_match_case = Checkbutton(root, text='Match case', variable=match_variable)
username_label.pack()
pass_label.pack()
username_entry.pack()
pass_entry.pack()
check_regular_expression.pack()
check_match_case.pack()
while True:
    print(regex_variable.get(), match_variable.get())
    if regex_variable.get() == 1:
        pass_entry.configure(show="")
        print("hi")
    else:
        pass_entry.configure(show="*")
        print("hi")
    root.update()
from tkinter import *
from tkinter import messagebox
import time
root = Tk()
root.title("Jumble Letters")
root.geometry("200x200")
main_button = Button(root, text="CLICK TO START", background="orange")
entry = Entry()


def main_button_command():
    main_button.config(text="GUESS THE JUMBLED WORD", background="orange")
    label = Label(text="enarhhfti")
    label.grid(row=1, column=0)


def submit_button():
    a = entry.get()
    if a == "fahrenheit":
        messagebox.showinfo("Good Job!", "You got it correct!")
        time.sleep(3)
        quit()
    else:
        messagebox.showerror("Incorrect!", "Try again!")



main_button = Button(root, text="CLICK TO START", fg="orange", command=main_button_command)
submit = Button(root, text="Submit", command=submit_button)
main_button.grid(row=0, column=0, columnspan=2, sticky="w")
entry.grid(row=1, column=1)
submit.grid(row=2, column=1)
root.mainloop()

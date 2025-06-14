from tkinter import *
import random
root = Tk()
root.geometry('375x100')
root.title("Random Generator")
label = Label(root, text="Give me a range ex: start-end")
random_number = StringVar()
answer_label = Label(root, textvariable=random_number)
entry = Entry(root)


def generate_button():
    global random_number
    a = []
    b = entry.get()
    a = b.split("-")
    answer = str(random.randint(int(a[0]), int(a[1])))
    random_number.set(answer)


generate = Button(root, text="generate", command=generate_button)
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
answer_label.grid(row=2, column=1)
generate.grid(row=1, column=1)
root.mainloop()

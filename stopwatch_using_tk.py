from tkinter import *
from tkinter import messagebox
import time
root = Tk()
root.title("Stopwatch")
root.geometry("200x200")
go = False
t = 0
original_t = 0
start_time = ""
text = Label(root, text="hi")


def start_command():
    global go
    global start_time
    global original_t
    global t
    go = True
    start_time = time.time()
    original_t = t


def stop_command():
    global go
    go = False


def reset_command():
    global t
    global original_t
    t = 0
    original_t = 0


start = Button(root, text="START", fg="green", command=start_command)
stop = Button(root, text="STOP", fg="red", command=stop_command)
reset = Button(root, text="RESET", fg="blue", command=reset_command)
text.grid(row=0, column=1)
start.grid(row=1, column=0)
stop.grid(row=1, column=1)
reset.grid(row=1, column=2)
while True:
    if go:
        t = original_t + time.time() - int(start_time)
    text.config(text=t)
    root.update()

from tkinter import *
import webcolors
import time
root = Tk()
root.title("RGB color picker")
red_var = IntVar()
green_var = IntVar()
blue_var = IntVar()
red_scale = Scale(root, label="red", variable=red_var, from_=0, to=255, orient=VERTICAL)
green_scale = Scale(root, label="green", variable=green_var, from_=0, to=255, orient=VERTICAL)
blue_scale = Scale(root, label="blue", variable=blue_var, from_=0, to=255, orient=VERTICAL)
label = Label(root)
red_scale.grid(row=0, column=0)
green_scale.grid(row=0, column=1)
blue_scale.grid(row=0, column=2)
label.grid(row=1, column=1)
while True:
    value = webcolors.rgb_to_hex((red_var.get(), green_var.get(), blue_var.get()))
    label.config(bg=value)
    root.update()

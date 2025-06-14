from tkinter import *

root = Tk()

#root.geometry("1000x750")
root.title("Calculator")
label = Label(root, text="", foreground='white', background="black", width=50, height=10, font=("Times New Roman", 20, "bold"))
label.pack()
entry = Entry(root, foreground="yellow", background="blue", width="75")
entry.insert(0, "Enter an expression here.")
entry.pack()
try:
    def addbutton():
        str = entry.get()
        s = str.split("+")
        a = ct.addition(int(s[0]), int(s[1]))
        #print(a)
        label.config(text = a)
        entry.delete(0, 100)
    def subtractbutton():
        str = entry.get()
        s = str.split("-")
        a = ct.subtraction(int(s[0]), int(s[1]))
        label.config(text = a)
        entry.delete(0, 100)
    def multiplybutton():
        str = entry.get()
        s = str.split("*")
        a = ct.multiplication(int(s[0]), int(s[1]))
        label.config(text=a)
        entry.delete(0, 100)
    def dividebutton():
        str = entry.get()
        s = str.split("/")
        a = ct.division(int(s[0]), int(s[1]))
        label.config(text=a)
        entry.delete(0, 100)

    abutton = Button(root, text="Add!", width=15, height=5, background="yellow", foreground="black", command=addbutton, font=("Times New Roman", 20, "bold"))
    abutton.pack(side=LEFT)
    sbutton = Button(root, text="Subtract!", width=15, height=5, background="yellow", foreground="black", command=subtractbutton, font=("Times New Roman", 20, "bold"))
    sbutton.pack(side=RIGHT)
    mbutton = Button(root, text="Multiply!", width=15, height=5, background="yellow", foreground="black", command=multiplybutton, font=("Times New Roman", 20, "bold"))
    mbutton.pack(side=LEFT)
    dbutton = Button(root, text="Divide!", width=15, height=5, background="yellow", foreground="black", command=dividebutton, font=("Times New Roman", 20, "bold"))
    dbutton.pack(side=RIGHT)
except ValueError:
    label.config(text = "An error occurred.")
root.mainloop()
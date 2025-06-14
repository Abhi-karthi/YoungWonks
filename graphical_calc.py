from math import sqrt
from tk_practice_2 import *
top = Tk()
top.title("Calculator")
top.configure(bg="black")
label1 = Label(top, bg="black", fg="white", font=("Times New Roman", 50))
entry1 = Entry(top, bg="white", fg="black")
entry1.insert(0, "Enter the first number here")
entry2 = Entry(top, bg="white", fg="black")
entry2.insert(0, "Enter the second number here")
label1.pack()
entry1.pack()
entry2.pack()


def add(num1, num2):
    global label1
    try:
        num1 = float(num1)
        num2 = float(num2)
        label1.config(text=f"{num1} + {num2} = {num1 + num2}")
        return num1, "+", num2, "=", num1 + num2
    except ValueError:
        label1.config(text="Please enter numbers.")


def subtract(num1, num2):
    global label1
    try:
        num1 = float(num1)
        num2 = float(num2)
        label1.config(text=f"{num1} - {num2} = {num1 - num2}")
        return num1, "-", num2, "=", num1 - num2
    except ValueError:
        label1.config(text="Please enter numbers.")
        return "Please enter numbers."


def multiply(num1, num2):
    global label1
    try:
        num1 = float(num1)
        num2 = float(num2)
        label1.config(text=f"{num1} x {num2} = {num1 * num2}")
        return num1, "x", num2, "=", num1 * num2
    except ValueError:
        label1.config(text="Please enter numbers.")


def divide(num1, num2):
    global label1
    try:
        num1 = float(num1)
        num2 = float(num2)
        if num2 != 0:
            label1.config(text=f"{num1} / {num2} = {num1 / num2}")
            return num1, "/", num2, "=", num1 / num2
        else:
            label1.config(text="You can't divide by zero: undefined")
            return "You can't divide by zero: undefined"
    except ValueError:
        label1.config(text="Please enter numbers.")


def exponent(num1, num2):
    global label1
    try:
        num1 = float(num1)
        num2 = float(num2)

        label1.config(text=f"{num1} ^ {num2} = {num1 ** (num2 ** num2)}")
        return num1, "^", num2, "=", num1 ** num2
    except ValueError:
        label1.config(text="Please enter numbers.")


def square_root(num1):
    global label1
    try:
        num1 = float(num1)
        try:
            label1.config(text=f"√{num1} = {sqrt(num1)}")
        except ValueError:
            label1.config(text=f"√{num1} = {sqrt(num1 * -1)}i")
    except ValueError:
        label1.config(text="Please enter a number.")
        
        
a = 0


def a_command():
    first = entry1.get()
    second = entry2.get()
    add(first, second)
    
    
def s_command():
    first = entry1.get()
    second = entry2.get()
    subtract(first, second)
    
    
def m_command():
    first = entry1.get()
    second = entry2.get()
    multiply(first, second)


def d_command():
    first = entry1.get()
    second = entry2.get()
    divide(first, second)
    
    
def r_command():
    first = entry1.get()
    square_root(first)


def e_command():
    first = entry1.get()
    second = entry2.get()
    exponent(first, second)
    
    
a_button = Button(top, text="+", font=("Arial", 100), command=a_command, bg="Black", fg="orange")
s_button = Button(top, text="-", font=("Arial", 100), command=s_command, bg="Black", fg="orange")
m_button = Button(top, text="x", font=("Arial", 100), command=m_command, bg="Black", fg="orange")
d_button = Button(top, text="/", font=("Arial", 100), command=d_command, bg="Black", fg="orange")
r_button = Button(top, text="√", font=("Arial", 100), command=r_command, bg="Black", fg="orange")
e_button = Button(top, text="^", font=("Arial", 100), command=e_command, bg="Black", fg="orange")
a_button.pack(side="left")
s_button.pack(side="right")
m_button.pack(side="left")
d_button.pack(side="right")
e_button.pack(side="left")
r_button.pack(side="right")
top.mainloop()

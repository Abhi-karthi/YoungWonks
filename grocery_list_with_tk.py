from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Grocery Store")
quantity = StringVar()
quantity.set("0")
enter_label = Label(root, text="Please enter an item:")
quantity_label = Label(root, text="Choose the quantity:")
amount_label = Label(root, textvariable=quantity)
text_box = Entry(root)
cart = {}


def minus_button():
    b = quantity.get()
    if int(b) > 0:
        a = int(b)
        a -= 1
        a = str(a)
        quantity.set(a)


def plus_button():
    b = quantity.get()
    a = int(b)
    a += 1
    a = str(a)
    quantity.set(a)


def add_to_cart_button():
    cart[text_box.get] = quantity.get
    text_box.delete(1, END)
    quantity.set("0")


def checkout_button():
    cart[text_box.get] = quantity.get
    text_box.delete(1, END)
    quantity.set("0")
    messagebox.showinfo("Checkout", str(cart))


minus = Button(root, text="-", fg="red", command=minus_button)
plus = Button(root, text="+", fg="green", command=plus_button)
add_to_cart = Button(root, text="Add to Cart", fg="green", command=add_to_cart_button)
checkout = Button(root, text="Checkout", fg="red", command=checkout_button)


enter_label.grid(row=0, column=0)
text_box.grid(row=0, column=1, columnspan=3)
minus.grid(row=2, column=1)
amount_label.grid(row=2, column=2)
plus.grid(row=2, column=3)
quantity_label.grid(row=1, column=1, columnspan=3)
add_to_cart.grid(row=1, column=0)
checkout.grid(row=2, column=0)

root.mainloop()

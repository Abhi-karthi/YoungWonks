from tkinter import *

root = Tk()
root.title("Calculator")
top_frame = Frame(root)
bottom_frame = Frame(root)

main_label_var = StringVar()
main_label = Label(top_frame, textvariable=main_label_var)
operations = []
numbers = []
operations_options = ("+", "-", "*", "/")
previous_label = ""

# Button Functions
def c_button_func():
    main_label_var.set("")


def decimal_point_button_func():
    main_label_var.set(f"{main_label_var.get()}.")


def plus_button_func():
    if main_label_var.get()[-1] not in operations_options:
        main_label_var.set(f"{main_label_var.get()}+")
        operations.append("+")


def minus_button_func():
    try:
        if main_label_var.get()[-1] not in operations_options:
            main_label_var.set(f"{main_label_var.get()}-")
            operations.append("-")
    except IndexError:
        pass


def multiply_button_func():
    try:
        if main_label_var.get()[-1] not in operations_options:
            main_label_var.set(f"{main_label_var.get()}*")
            operations.append("*")
    except IndexError:
        pass


def divide_button_func():
    try:
        if main_label_var.get()[-1] not in operations_options:
            main_label_var.set(f"{main_label_var.get()}/")
            operations.append("/")
    except IndexError:
        pass


def delete_button_func():
    if len(main_label_var.get()) > 0:
        if main_label_var.get()[-1] in operations_options:
            operations.pop(-1)
        main_label_var.set(main_label_var.get()[0:-1])

def equal_button_func():
    global previous_label

    if main_label_var.get()[-1] not in operations_options:

        previous_label = main_label_var
        number_sections = []
        current_number = ""

        for i in main_label_var.get():
            if i in operations_options:
                number_sections.append(float(current_number))
                current_number = ""
            else:
                current_number += i
        number_sections.append(float(current_number))
        operation_count = 0
        for i in range(len(main_label_var.get())):
            print(number_sections)
            if main_label_var.get()[i] == "/":
                operation_count += 1
                try:
                    number_sections[operation_count - 1] /= number_sections[operation_count]
                except ZeroDivisionError:
                    print("Error: Can't divide by zero")
                    main_label_var.set("")
                    break

                number_sections.pop(operation_count)

            if main_label_var.get()[i] == "*":
                operation_count += 1
                # print(operation_count)
                number_sections[operation_count - 1] *= number_sections[operation_count]
                number_sections.pop(operation_count)

        operation_count = 0
        for i in range(len(main_label_var.get())):
            print(number_sections)
            if main_label_var.get()[i] == "+":
                operation_count += 1
                number_sections[operation_count - 1] += number_sections[operation_count]
                number_sections.pop(operation_count)

            if main_label_var.get()[i] == "-":
                operation_count += 1
                number_sections[operation_count - 1] -= number_sections[operation_count]
                number_sections.pop(operation_count)


        main_label_var.set(str(number_sections[0]))


#Number functions
def button0_function():
    main_label_var.set(f"{main_label_var.get()}0")


def button1_function():
    main_label_var.set(f"{main_label_var.get()}1")


def button2_function():
    main_label_var.set(f"{main_label_var.get()}2")


def button3_function():
    main_label_var.set(f"{main_label_var.get()}3")


def button4_function():
    main_label_var.set(f"{main_label_var.get()}4")


def button5_function():
    main_label_var.set(f"{main_label_var.get()}5")


def button6_function():
    main_label_var.set(f"{main_label_var.get()}6")


def button7_function():
    main_label_var.set(f"{main_label_var.get()}7")


def button8_function():
    main_label_var.set(f"{main_label_var.get()}8")


def button9_function():
    main_label_var.set(f"{main_label_var.get()}9")


# Button Initialization
c_button = Button(bottom_frame, text="C", command=c_button_func)
delete_button = Button(bottom_frame, text="Del", command=delete_button_func)
plus_button = Button(bottom_frame, text="+", command=plus_button_func)
minus_button = Button(bottom_frame, text="-", command=minus_button_func)
multiply_button = Button(bottom_frame, text="*", command=multiply_button_func)
divide_button = Button(bottom_frame, text="/", command=divide_button_func)
equal_button = Button(bottom_frame, text="=", command=equal_button_func)
button1 = Button(bottom_frame, text="1", command=button1_function)
button2 = Button(bottom_frame, text="2", command=button2_function)
button3 = Button(bottom_frame, text="3", command=button3_function)
button4 = Button(bottom_frame, text="4", command=button4_function)
button5 = Button(bottom_frame, text="5", command=button5_function)
button6 = Button(bottom_frame, text="6", command=button6_function)
button7 = Button(bottom_frame, text="7", command=button7_function)
button8 = Button(bottom_frame, text="8", command=button8_function)
button9 = Button(bottom_frame, text="9", command=button9_function)
button0 = Button(bottom_frame, text="0", command=button0_function)
decimal_point_button = Button(bottom_frame, text=".", command=decimal_point_button_func)

# Packing
top_frame.grid(row=0, column=0)
bottom_frame.grid(row=1, column=0)

main_label.grid(row=0, column=0)
c_button.grid(row=0, column=1)
delete_button.grid(row=0, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
divide_button.grid(row=1, column=3)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
multiply_button.grid(row=2, column=3)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
minus_button.grid(row=3, column=3)
button0.grid(row=4, column=0)
decimal_point_button.grid(row=4, column=1)
equal_button.grid(row=4, column=2)
plus_button.grid(row=4, column=3)

root.mainloop()

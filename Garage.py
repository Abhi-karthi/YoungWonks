from tk_practice_2 import *
top = Tk()
label1 = Label(top, font=("Times New Roman", 50))
entry1 = Entry(top, font=("Times new Roman", 25))
b = None


class Garage:
    def __init__(self, number, color, model, brand):
        super().__init__(number)
        self.color = color
        self.model = model
        self.brand = brand

    def change(self):
        global entry1
        entry1.insert(0, "Do you want to change your cars color? Enter 'yes' or 'no' (caps sensitive). Press return or enter when done. ")
        def if_color():
            global entry1
            global label1
            a = entry1.get()
            if a == "yes":
                label1.config(text="You have many options to choose from. Enter a color in lowercase and I will tell you if it's valid.")
                def color_valid():
                    colorr = entry1.get()
                    if colorr == "red" or colorr == "orange" or colorr == "yellow" or colorr == "green" or colorr == "blue" or colorr == "purple" or colorr == "magenta" or colorr == "brown" or colorr == "black" or colorr == "white" or colorr == "grey":
                        self.colorr = colorr
                    elif colorr == "valid colors":
                        label1.config(font=("Arial", 5), text="'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'magenta', 'brown', 'black', 'white', and 'gray' are the valid colors. ")
                    elif colorr == "cancel":
                        pass
                    else:
                        label1.config(font=("Arial", 15), text="Color not valid. Type in 'valid colors' to see all valid colors. Type 'cancel' to cancel.")
            elif a == "no":
                label1.config(text="Okay.")
            entry1.bind('<Return>', if_color)


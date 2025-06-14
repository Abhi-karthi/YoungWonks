from tkinter import *
root = Tk()
root.title("Checkboxes")
q_number = 1


class Question:
    def submit_button_command(self):
        if self.radio_var.get() == self.options.index(self.answer):
            self.item_list[self.options.index(self.answer) + 1].config(fg='green')
        else:
            self.item_list[self.options.index(self.answer) + 1].config(fg='green')
            self.item_list[self.options[self.radio_var.get()-1]].config(fg='red')


    def __init__(self, options: list, answer: str, question: str):
        self.frame = Frame(root)
        self.options = options
        self.answer = answer
        self.question = question
        self.radio_var = IntVar()
        self.submit_button = Button(self.frame, text='Submit', )
        self.item_list = []

    def show(self):
        self.item_list[0] = Label(self.frame, text=self.question)
        self.item_list[0].grid(row=)
        for i in range(len(self.options)):
            self.item_list[i + 1] = Radiobutton(self.frame, text=self.options[i], variable=self.radio_var, value=i)



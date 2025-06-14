from tkinter import *

root = Tk()
root.title("Quiz")
mainframe = Frame(root, bg="grey")
score = 0
next_available = False


class Question:
    def __init__(self, question: str, choices: list, answer: int):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.question_label = Label(mainframe, text=self.question)
        self.radio_var = IntVar()
        self.choices_button = []
        for i in self.choices:
            self.choices_button.append(Radiobutton(mainframe, text=i, variable=self.radio_var, value=self.choices.index(i) + 1))

    def submit(self):
        global score
        global next_available
        if self.radio_var.get() == self.answer:
            score += 1
        else:
            self.choices[self.radio_var.get() - 1].config(fg="red")
        self.choices[self.answer - 1].config(fg="green")
        next_available = True
        

root.mainloop()
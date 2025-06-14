def question1(equation: str):
    equation_list = []
    answers = []
    for i in equation:
        equation_list.append(i)
    if "(" in equation_list:
        value = equation_list.index("(")
        for i in range(len(equation_list) + 2):
            if i > value + 3 and i%2 == 1:
                answers.append(i)
    elif ")" in equation_list:
        value = equation_list.index(")")
        for i in range(len(equation_list)):
            if i < value and i % 2 == 1:
                answers.append(i)

    return answers


print(question1("6+2/3*4)"))


def question2()
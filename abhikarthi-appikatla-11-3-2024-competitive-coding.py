def question1(options: list, expression: str):
    expression_list = expression.split()
    operation = []
    operations = ["*", "?", "+"]
    answers = []
    answer_test = ""
    for i in expression_list:
        if i in operations:
            operation.append(i)

    for i in operations:
        if i == "?":
            expression.index("?") - 1



sample_input_options = ["#", "a", "aa", "aaa", "ab", "abb", "aabb", "aaab", "abbb", "b"]

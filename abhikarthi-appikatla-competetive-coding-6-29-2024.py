# Program 1
from typing import List


def list_sum(n: int, x: int, array: list) -> list and str:
    """

    :rtype: object
    """
    answers = []
    for i in array:
        for a in array:
            if array.index(i) != array.index(a):
                if i + a == x:
                    if (array.index(i) + 1, array.index(a) + 1) not in answers:
                        if (array.index(a) + 1, array.index(i) + 1) not in answers:
                            if i > a:
                                answers.append((array.index(i) + 1, array.index(a) + 1))
                            elif i < a:
                                answers.append((array.index(a) + 1, array.index(i) + 1))
                            else:
                                answers.append((array.index(i) + 1, array.index(a) + 1))
    if len(answers) == 0:
        return "IMPOSSIBLE"
    else:
        return answers


list_sample: list[int] = [2, 2, 1, 0, 3]
answer = list_sum(2, 3, list_sample)
if answer != "IMPOSSIBLE":
    for i in answer:
        for x in i:
            print(x, end=" ")
        print()
else:
    print(answer)
# Problem 2


def

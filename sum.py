import json


def add(n1, n2):
    answer = 0
    for i in range(n1):
        answer += 1
    for i in range(n2):
        answer += 1
    return answer


def subtract(n1, n2):
    answer = 0
    for i in range(n1):
        answer += 1
    for i in range(n2):
        answer -= 1
    return answer


def multiply(n1, n2):
    answer = 0
    for i in range(n1):
        answer += n2
    return answer


def divide(n1, n2):
    answer = 0


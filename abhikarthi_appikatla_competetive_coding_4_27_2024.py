# Program 1
def calculate_average(numbers: list):
    add = 0
    for i in numbers:
        add += i
    return add/len(numbers)


sample_input = [10, 20, 30, 40, 50]
print(calculate_average(sample_input))
# Program 2


def find_maximum(numbers: list):
    answer = numbers[0]
    for i in numbers:
        if i > answer:
            answer = i
    return answer


sample_input = [10, 20, 5, 35, 25]
print(find_maximum(sample_input))
# Program 3


def generate_fibonacci(n):
    answer = []
    for i in range(n):
        if len(answer) == 0:
            answer.append(0)
        elif len(answer) == 1:
            answer.append(1)
        else:
            answer.append(answer[-1] + answer[-2])
    return answer


sample_input = 7
print(generate_fibonacci(sample_input))
# Program 4


def is_non_prime(n):
    if n < 2:
        return False
    else:
        answer = True
        for i in range(2, n):
            if n % i == 0:
                answer = False
            print("H")
        if answer:
            return False
        else:
            return True


sample_input = 12
print(is_non_prime(sample_input))
# Program 5


def power(base: int, exponent: int):
    answer = base
    for i in range(exponent - 1):
        answer *= base
    return answer


base = 2
exponent = 5
print(power(base, exponent))

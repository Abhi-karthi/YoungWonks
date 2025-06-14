def fibonacci(number: int):
    total = [0]
    for i in range(number - 1):
        if len(total) < 2:
            total.append(1)
        else:
            total.append(total[-1] + total[-2])

    return total

def fibonacci_recursive(amount: int, current_number: int, prev_number: int):
    if amount < 1:
        return 0
    else:
        current_number = current_number + prev_number
        prev_number = current_number - prev_number
        amount -= 1
        print(current_number)
        fibonacci_recursive(amount, current_number, prev_number)


answer = 0
def sum_of_number_digits(number: int):
    global answer
    if number == 0:
        return 0
    else:
        answer = answer + number%10
        return sum_of_number_digits(number//10)



answer_for_string_reverser = ""
# def string_reverser(word: str):
#     if len(answer_for_string_reverser) == len(word):
#         return 0
#     else:



print(fibonacci_recursive(10000, 0, 0))


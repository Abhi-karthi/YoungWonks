# Program 1
def find_missing_integer(list_of_integers: list):
    prev = list_of_integers[0]
    answer = 0
    for i in list_of_integers[1:]:
        if i-prev != -1 and i-prev != 1:
            if prev > i:
                answer = prev - 1
                break
            else:
                answer = i - 1
                break
        prev = i
    return answer


print(find_missing_integer([1, 2, 4, 5, 6, 7]))
# Program 2


def find_gcd(x: int, y: int):
    num_list = []
    answer = 0
    if x >= y:
        for i in range(1, x):
            num_list.insert(0, i)
    else:
        for i in range(1, y):
            num_list.insert(0, i)
    # print(num_list)
    for i in num_list:
        if x % i == 0 and y % i == 0:
            answer = i
            break
    return answer


print(find_gcd(12, 18))
# Program 3


def number_of_divisors(number: int):
    answer = 0
    for i in range(1, number + 1):
        if number % i == 0:
            answer += 1
    return answer


print(number_of_divisors(10))
# Program 4


# def length_of_the_longest_increasing_subsequence(list_of_integers: list):
#     answer = []
#     temp = 0
#     for i in list_of_integers:
#


# Program 1
def number_of_divisors(number_of_numbers: int, numbers: list):
    integers = []
    for i in range(len(numbers)):
        integers.append(0)
        for x in range(numbers[i]):
            if numbers[i] > 0:
                if numbers[i] % x == 0:
                    integers[i] += 1
    return integers

sample = 4
sample2 = [12, 25, 36, 49]
print(number_of_divisors(sample, sample2))

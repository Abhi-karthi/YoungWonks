# Problem 2
def problem2(n: int, integers: list):
    ordered_list = []
    i = n
    median = 0
    differences = []
    add = 0
    while i >= 0:
        ordered_list.append(min(integers))
        integers.remove(min(integers))
        i -= 1
    if n % .5 == 0:
        median = ordered_list[int(n/2)]
    else:
        median = ordered_list[int(n/2)]
    for i in ordered_list:
        if i - median < 0:
            differences.append((i-median)*-1)
        elif i - median > 0:
            differences.append((i-median))
        else:
            differences.append(0)
    for i in differences:
        add += i
    print(f"${add}")


problem2(5, [5, 2, 7, 4, 8, 9])
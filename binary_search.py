# import time
# import random
#
# main_list = []
# for i in range(1, 10000000):
#     main_list.append(i)
#     print(i)
#
# print("finished list")
#
# target = 10000000 - 2749
#
# minimum = 0
# maximum = len(main_list) - 1
# mid = 0
# cycles = 0
#
# success = False
# start = time.time()
#
# while minimum < maximum:
#     cycles += 1
#     mid = (maximum + minimum) // 2
#     if main_list[mid] == target:
#         success = True
#         break
#     elif main_list[mid] < target:
#         minimum = mid + 1
#     elif main_list[mid] > target:
#         maximum = mid - 1
#
# timer = time.time() - start
# print(timer, cycles)
# if success:
#     print(f"present at index {mid}")
# else:
#     print("Not present")
#

# full_array = [2, 5, 6, 7, 10, 25, 26]
# target = 250
# minimum = 0
# maximum = len(full_array) - 1
# success = False
# mid = 0
def b_func(full_array, target, minimum, maximum, success, mid):
    if minimum > maximum or success:
        if success:
            return mid
        else:
            return None
    else:
        mid = (maximum + minimum) // 2
        if full_array[mid] == target:
            success = True
        elif full_array[mid] < target:
            minimum = mid + 1
        elif full_array[mid] > target:
            maximum = mid - 1
        return b_func(full_array, target, minimum, maximum, success, mid)


def binary_search(array: list, value):
    full_array = array
    target = value
    minimum = 0
    maximum = len(full_array) - 1
    success = False
    mid = 0

    return b_func(full_array, target, minimum, maximum, success, mid)

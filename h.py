def digit_sum(digits,n):
        if "0" not in list(digits):
            if n > 0:
                while len(digits) > n:
                    result = list(digits)
                    digits = 0
                    for i in range(len(result)):
                        digits += int(result[i])
                    digits = str(digits)
                    #print(digits)
                return digits
            else:
                return -1
        else:
            return 0
def check(digits):
    if len(digits) == 16:
        try:
            int(digits)
            return True
        except ValueError:
            return False
    else:
        return False

from binary_search import binary_search

print(binary_search([1, 2, 3, 4, 5, 6, 7], 2))
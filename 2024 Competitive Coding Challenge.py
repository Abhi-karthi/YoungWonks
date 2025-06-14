# Program one:

n = int(input("Enter an integer: "))
my_range = range(1, n + 1)
for i in my_range:
    if i % 2 == 0:
        print(i)
# Program two:

list_of_numbers = []
new_list = []
used_list = []
for i in range(10):
    a = int(input(f"Enter integer number {i + 1} please: "))
    list_of_numbers.append(a)

for i in list_of_numbers:
    if i in new_list and i not in used_list:
        print(i)
        used_list.append(i)
    else:
        new_list.append(i)
# Program 3

palindrome_number = int(input("Please enter an integer: "))
palindrome_number = str(palindrome_number)
palindrome = True
for i in range(len(palindrome_number)):
    if palindrome_number[i] != palindrome_number[-i - 1]:
        palindrome = False
if palindrome:
    print("Palindrome")
else:
    print("Not palindrome")

# Program 4

n = int(input("Enter a number: "))
prime = True
for i in range(n):
    if i > 1:
        if n % i == 0:
            prime = False
if prime:
    print("Yes")
else:
    print("No")

# Program 5

sum = 0
numbers = [[46, 24], [30, 17], [76, 0], [75, 70], [35, 49], [8, 19], [27, 91], [12, 3], [69, 71], [61, 38]]
for i in numbers:
    for x in i:
        sum += x
print(sum)
# Program 1

def program1(n):
    numsum = 0
    for i in range(1, n+1):
        numsum = 0
        for x in str(i):
            numsum += int(x)

        if i % numsum == 0:
            print(i)

# Program 2

def program2(factorial):
    factorial_output = 1
    if factorial > 0:
        for i in range(1, factorial + 1):
            factorial_output *= i
        print(factorial_output)
    else:
        if factorial == 0:
            print(1)
        else:
            print("Please enter a positive integer.")

# Program 3

def program3(items):
    for i in range(len(items)+1):
        i *= -1
        print(items[i], len(items[i]))

# Program 4
def program4():
    for i in range(1680, 1740 + 1):
        if i % 4 == 0:
            print(i)

# Program 5
def program5(fib):
    counter = 0
    prevcounter = 0
    for i in range(1, fib + 1):
        print(f"{counter} ", end="")
        if counter == 0:
            counter += 1
        else:
            counter += prevcounter
            prevcounter = counter - prevcounter


n = int(input("Enter an integer: "))
program1(n)
factorial = int(int(input("Enter a positive integer: ")))
program2(factorial)
items = ["Orange", "Banana", "Apple"]
program3(items)
program4()
fib = int(input("Enter an integer: "))
program5(fib)

def collatz(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence

def test_collatz(limit):
    for num in range(1, limit + 1):
        sequence = collatz(num)
        if sequence[-1] != 1:
            print(f"Collatz conjecture failed for {num}: {sequence}")

try:
    limit = int(input("Enter a positive integer limit for testing: "))
    if limit <= 0:
        print("Please enter a positive integer limit.")
    else:
        test_collatz(limit)
except ValueError:
    print("Invalid input. Please enter a positive integer limit.")


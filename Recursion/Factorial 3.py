def factorial(n):
    if n == 0:  # Base case
        return 1
    elif n <= 13:  # Recursive case
        return n * factorial(n - 1)
    else:
        return ("input too large")

t = int(input()) # num. test cases
if t == 0:
    exit()

for i in range(t):
    n = int(input()) # factorial
    if n <= 13:
        print(factorial(n))
    else:
        print("input too large")
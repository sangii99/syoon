def factorial(n):
    if n == 0:  # Base case
        return 1
    return n * factorial(n - 1)
t = int(input()) # num. test cases

for i in range(t):
    n = int(input()) # factorial
    print(factorial(n) if n <= 13 else "input too large")
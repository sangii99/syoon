t = int(input()) # test cases
if t == 0:
    sys.exit


n = int(input()) # factorial number
def factorial(n):
    if n == 0:  # Base case
        return 1
    elif n <= 13:       # Recursive case
        return n * factorial(n - 1)
    else:
        return("input too large")

print(factorial(n))
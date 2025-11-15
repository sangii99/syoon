'''def iszigzag(x):
    odd = 0
    even = 1
    for i in range(len(x)):
        if x[i] <= x[i+1] and x[i+1] >= x[i+2]:
            i += i+2
        else:
            return False
'''

x = [10, 5, 6, 3, 2, 20, 100, 80, 30]
def iszigzag(x):
    odd, even = [], []
    for i in range(len(x)):
        if i % 2 == 0:
            odd.append(x[i])
        else:
            even.append(x[i])

    odd_even = 0
    even_odd = 0
    y = len(even)
    for t in range(y):
        if even[t] > odd[t]:
            even_odd += 1
        elif odd[t] > even[t]:
            odd_even += 1
    if len(odd) > len(even):
        last_num = odd[len(odd) - 1]
        if last_num >= even[y-1]:
            odd_even += 1
        else:
            even_odd += 1

    if even_odd > odd_even:
        return False
    elif odd_even > even_odd and even_odd ==0:
        return True
    elif odd_even == even_odd == 0:
        return True
    else:
        return False

print(odd_even, even_odd)









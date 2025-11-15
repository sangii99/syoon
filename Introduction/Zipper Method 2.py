
def weave(x, y):
    ans = []
    if len(x) < len(y):
        for i in range(len(x)):
            for j in range(len(y)):
                ans.append(x[i])
                ans.append(y[j])
    elif len(x) > len(y):
        for i in range(len(y)):
            for j in range(len(x)):
                ans.append(x[j])
                ans.append(y[i])
    else:
        for i in range(len(x)):
            ans.append(x[i])
            ans.append(y[i])
    return ans


x, y = ('A', 'B', 'C'),  [1, 2]
def weave(x, y):
    ans = []
    a, b = len(x), len(y)
    if a > b:
        for i in range(a):
            ans.append(x[i])
            ans.append(y[i % b])
    elif a < b:
        for i in range(b):
            ans.append(x[i])
            ans.append(y[i % a])
    else:
        for i in range(a):
            ans.append(x[i])
            ans.append(y[i])
    return ans
def zipper(x, y):
    ans = []
    a, b = len(x), len(y)
    maxim = max(a, b)
    if a > b:
        for i in range(maxim):
            if i < a:
                ans.append(x[i])
            if i < b:
                ans.append(y[i])
    elif a < b:
        for i in range(maxim):
            if i < a:
                ans.append(x[i])
            if i < b:
                ans.append(y[i])
    else:
        for i in range(a):
            ans.append(x[i])
            ans.append(y[i])
    return ans

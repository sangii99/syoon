def merge(a, b):
    num = 0
    merged = []
    if len(a) < len(b):
        num = len(a)
    else:
        num = len(b)
    for i in range(num):
        merged.append(a[i])
        merged.append(b[i])
    return merged

def weave(a, b):
    num = 0
    weaved = [[a[i], b[i] for i in range(len(a))]
    ]
'''x, y = [3, 9, -4, 2, 5], -3
def combisum(x, y):
    sums = []
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            sums.append(x[i] + x[j])
    sums.sort()
    low = 0
    high = len(x) - 1
    while high >= low:
        mid = (low + high) // 2
        if y < sums[mid]:
            high = mid - 1
        elif y == sums[mid]:
            return True
        else:
            low = mid + 1
    return False
'''


x, y = [-4, 2, 3, 5, 9], -3

sums = []
for i in range(len(x)):
    for j in range(i + 1, len(x)):
        sums.append(x[i] + x[j])
sums.sort()
low = 0
high = len(sums) - 1
while high >= low:
    mid = (low + high) // 2
    if y < sums[mid]:
        high = mid - 1
    elif y == sums[mid]:
        print("True")
        break
    else:
        low = mid + 1
print("False")
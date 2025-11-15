x = [-11, -32, 49, 9, 100, 55, 43, -33, 46]
print(sorted(x))
y = [-11, -32, 49, 9, 100, 55, 43, -33]
'''
def iszigzag(x):
    zigzag = 0
    num = len(x)
    if num % 2 == 0:
        for i in range(0, num - 1):
            if x[i] >= x[i+1]:
                zigzag += 1
        if num / 2 == zigzag:
            return True
        else:
            return False
    else:
        for i in range(0, num):
            if x[i] >= x[i+1]:
                zigzag += 1
        if (num - 1) / 2 == zigzag:
            return True
        else:
            return False
couples = []
'''
couples = []
for i in range(len(x) - 1):
    a=x[i]
    b=x[i+1]
    couples.append([a, b])

def iszigzag(x):
    couples = []
    for i in range(len(x) - 1):
        a = x[i]
        b = x[i + 1]
        couples.append([a, b])
    count = 0
    for t in range(len(couples)):
        a = couples[t]
        if (t + 1) % 2 != 0:  # odd index : first_num >= second_num
            if a[0] >= a[1]:
                count += 1
            else:
                count -= 1
        elif (t + 1) % 2 == 0:  # even index: first_num <= second_num
            if a[0] <= a[1]:
                count += 1
            else:
                count -= 1
    if count == len(couples):
        return True
    else:
        return False

def zigzag_slow(seq):
    seq.sort()
    couples = [(seq[i], seq[i+1]) for i in range(0, len(seq) - 1, 2)]
    last_num = None
    if len(seq) % 2 != 0:
        last_num = seq[len(seq) - 1]
    zigzagseq = []
    for a, b in couples:
        zigzagseq.append(b)
        zigzagseq.append(a)

    if last_num != None:
        zigzagseq.append(last_num)
    seq[:] = zigzagseq
    return None

seq = [1, 2, 3]
zigzag_slow(seq)
print(seq)

def zigzag_slow(seq):
    seq.sort()  # sort in-place
    # pair up elements
    pairs = [(seq[i], seq[i+1]) for i in range(0, len(seq) - 1, 2)]
    last_num = None
    if len(seq) % 2 != 0:
        last_num = seq[-1]  # last element if odd length

    # build zigzag sequence
    zigzagseq = []
    for a, b in pairs:
        zigzagseq.append(b)  # swap order to create zigzag
        zigzagseq.append(a)

    if last_num is not None:
        zigzagseq.append(last_num)

    # modify seq in-place
    seq[:] = zigzagseq
    return None

seq = [1, 2, 3]
zigzag_slow(seq)
print(seq)

def zigzag_fast(seq):
    for i in range(0, len(seq), 2):
        if  i - 1 >= 0 and seq[i] <= seq[i - 1]: # swap previous odd with current even pos
            seq[i], seq[i - 1] = seq[i - 1], seq[i]
        if i + 1 <= (len(seq) - 1) and seq[i] <= seq[i + 1]: # swap next odd with current even pos
            seq[i], seq[i+1] = seq[i+1], seq[i]
    return None


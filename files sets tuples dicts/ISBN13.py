def isISBN13(code):
    if not (
        isinstance(code, str) and
        len(code) == 13 and
        code.isdigit()
    ):
        return False
    if code[:3] not in {'978', '979'}:
        return False

    checkdigit = sum((3 if i % 2 else 1) * int(code[i]) for i in range(12))
    checkdigit = (10 - checkdigit % 10) % 10

    return checkdigit == int(code[-1])

def overview(codes):
    groups = {}
    for i in range(11):
        groups[i] = 0
    for code in codes:
        if not isISBN13(code):
            groups[10] += 1
        else:
            groups[int(code[3])] += 1

    print('English speaking countries: {}'.format(groups[0] + groups[1]))
    print('French speaking countries: {}'.format(groups[2]))
    print('German speaking countries: {}'.format(groups[3]))
    print('Japan: {}'.format(groups[4]))
    print('Russian speaking countries: {}'.format(groups[5]))
    print('China: {}'.format(groups[7]))
    print('Other countries: {}'.format(groups[6] + groups[8] + groups[9]))
    print('Errors: {}'.format(groups[10]))
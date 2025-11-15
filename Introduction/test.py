def isISBN(code):
    if not isinstance(code, str): # if the code isn't a string value, return False
        return False
    groups = code.split('-') # we split the code into tuples according to '-'
    if tuple(len(i) for i in groups) != (1, 4, 4, 1): #the correct isbn code has 4 groups, which has 1, 4, 4, and 1 digit each group
        return False #return false if not the case
    code = ''.join(groups) #we join the groups back
    if len(code) != 10: #if the code length is not 10, meaning there aren't 10 digits, return false
        return False
    if not code[:-1].isdigit(): # if the first 9 digits aren't numbers, return false
        return False
    return check(code) == code[-1] # last number of isbn is the checker, so we save that value as a variable
def check(code):
    check = sum((i + 1) * int(code[i]) for i in range(9)) % 11
    return 'X' if check == 10 else str(check) #put if statement to check if the code is correct or wrong.
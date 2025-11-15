# Yoon, Sang
# 01815283

def heads(coins):
    '''
>>> heads('THHTHTHHTHH')
7
>>> heads('HHHHTTTHTHT')
6
>>> heads('THTHTTTHTTH')
4

    '''

    headcount = 0 # variable to keep headcount
    for i in str(coins):
        if i.upper() == 'H':
            headcount += 1 # add to headcount if iterable in str(coins) is 'H'
    return headcount

def tails(coins):

    '''
>>> tails('THHTHTHHTHH')
4
>>> tails('HHHHTTTHTHT')
5
>>> tails('THTHTTTHTTH')
7
    '''
    tailcount = 0 # variable to keep tailcount
    for j in str(coins):
        if j.upper() == 'T':
            tailcount += 1 # add to tailcount if we see tail ('T')
    return tailcount

def you_more_heads_than_me (my_coins, your_coins):
    '''
>>> you_more_heads_than_me('THHTH', 'THHTHH')
True
>>> you_more_heads_than_me('HHHHT', 'TTHTHT')
False
>>> you_more_heads_than_me('THTHT', 'TTHTTH')
False
    '''

    my_heads = heads(my_coins) # get the headcount of each person's tosses
    your_heads = heads(your_coins)
    if your_heads > my_heads: # return True if you have more heads than me
        return True
    return False

def outcome(my_tosses, your_tosses, decimal):
    '''
>>> outcome(5, 6, 1188)
('THHTH', 'THHTHH')
>>> outcome(5, 6, 117)
('HHHHT', 'TTHTHT')
>>> outcome(5, 6, 1398)
('THTHT', 'TTHTTH')
>>> outcome(0, 1, 1)
('', 'T')
    '''

    sum_of_tosses = int(my_tosses) + int(your_tosses)
    number = bin(decimal)[2:] # use decimal to get binary version of it, cut off '0b' in the front
    sequence = str()
    if sum_of_tosses - len(number) > 0:
        number = '0' * (sum_of_tosses - len(number)) + number # add 0's to the front of the binary number so that we can match the number of digits
    for i in number:                                          # with the number of tosses
        if i == '0':
            sequence += 'H'
        else:
            sequence += 'T'   # create another sequence corresponding to the binary numbers (0 = h, 1 = t)
    my_throws = sequence[0:my_tosses] # use string slicing to cut the sequence into two parts (my, your)
    your_throws = sequence[my_tosses:]
    return ((my_throws, your_throws)) # return in tuple value

def probability(my_tosses, your_tosses):
    '''
>>> probability(5, 6)
0.5
>>> probability(6, 5)
0.2744140625
>>> probability(3, 8)
0.88671875
    '''


    total_tosses = my_tosses + your_tosses
    possibilities = 2 ** total_tosses # get total possibilities (used to calculate probability later)
    occurences = 0 # keep count of total occurences of yourheads > myheads
    number = str()
    sequence = str()
    if int(my_tosses) == 0 and int(your_tosses) == 0: # if nobody throws, no possibility, so return 0
        return 0
    else:
        for decimal in range(possibilities): # iterate through all the possibilities
            my_throws, your_throws = outcome(my_tosses, your_tosses, decimal) # get the sequences of mythrows and yourthrows (unpacking tuple)
            if you_more_heads_than_me(my_throws, your_throws): # if you have more heads than me add to count
                occurences += 1
    return float(occurences/possibilities) # return the final probability




if __name__ == '__main__':
    import doctest
    doctest.testmod()
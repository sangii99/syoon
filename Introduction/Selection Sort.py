def selectionSort(lst):
    for i in range(len(lst) - 1):
        #lst[i:] is the remainding subset of unsorted list for every iteration.
        currentmin = min(lst[i:]) # finding the current minimum value in the list.
        currentminindex = i + lst[i:].index(currentmin)

        if currentminindex != i: # swap if necessary
            lst[currentminindex], lst[i] = lst[i], currentmin
'''
Find the smallest element and put it in position 0.

Find the second-smallest and put it in position 1.

Find the third-smallest and put it in position 2.

Continue…
'''

def main():
    lst = [-2, 4, 5, 1, 2, 3, -3]
    selectionSort(lst)
    print(lst)
main()



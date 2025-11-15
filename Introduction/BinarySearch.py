'''
def search(sorted_list: list, x: int):
    for i in range(len(sorted_list)):
        if sorted_list[i] == x:
            return i-1
        elif sorted_list[i] < x:
            return -1
        elif sorted_list[i] > x:
            return 1
        else:
            return None

'''



def binarySearch(lst, key):
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = (low+high)//2
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            high = mid-1
        else:
            low = mid+1

    return - low - 1

def main():
    lst = [-3, 1, 2, 4, 9, 23]
    print(binarySearch(lst, 1))

main()





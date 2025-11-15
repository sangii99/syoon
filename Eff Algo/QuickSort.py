def sort(list):
    quicksorthelper(list, 0, len(list)-1)

def quicksorthelper(list, start, end):
    if end > start:
        pivotindex = partition(list, start, end)
        quicksorthelper(list, start, pivotindex-1)
        quicksorthelper(list, pivotindex+1, end)


def partition(list, start, end):
    pivot = list[start]
    low = start+1
    high = end
    while high > low:
        while low <= high and list[low] <= pivot:
            low += 1

        while low <= high and list[high] > pivot:
            high -= 1

        if high > low:
            list[low], list[high] = list[high], list[low]

    while high > start and list[high] >= pivot:
        high -= 1

    if pivot > list[high]:
        list[start] = list[high]
        list[high] = pivot
        return high
    else:
        return start




from Heap.py import Heap
class PriorityQueue:
    def __init__(self):
        self.__heap = Heap()

    def enqueue(self, item):
        self.__heap.add(item)

    def dequeue(self):
        if self.getSize() == 0:
            return None
        else:
            return self.__heap.remove()

    def getSize(self):
        return self.__heap.getSize()

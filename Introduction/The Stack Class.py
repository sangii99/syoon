class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def peek(self):
        if self.isEmpty():
            return None
        return self.__elements[len(self.__elements) - 1]

    def push(self, item):
        self.__elements.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.__elements.pop()

    def getSize(self):
        return len(self.__elements)
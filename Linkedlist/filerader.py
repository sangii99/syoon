import csv

class Linked_List_Node:
    def __init__(self, task_name, duration, priority):
        self.task_name = task_name
        self.duration = int(duration)
        self.priority = int(priority)
        self.next = None

class Linked_List:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def read_tasks_from_csv(self, filepath):
        with open(filepath, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            # skip header if present
            first = next(reader, None)
            if first and not first[1].isdigit():
                pass
            else:
                if first:
                    self.add_task(first[0], int(first[1]), int(first[2]))
            for row in reader:
                self.add_task(row[0], int(row[1]), int(row[2]))

    def add_task(self, task_name, duration, priority):
        newnode = Linked_List_Node(task_name, duration, priority)
        if self.__tail is None: # == if the list is empty
            self.__head = self.__tail = newnode
        else: # make the pointer point at the newnode
            self.__tail.next = newnode
            self.__tail = newnode
        self.__size += 1

    def find_task(self, task_name):
        current = self.__head
        while current:
            if current.task_name == task_name:
                return current
            current = current.next
        return None

    def display_tasks(self):
        current = self.__head
        while current:
            print(current.task_name)
            current = current.next

    def calculate_total_duration(self):
        total = 0
        current = self.__head
        while current:
            total += current.duration
            current = current.next
        return total

    def remove_task(self, task_name):
        prev = None
        curr = self.__head
        while curr:
            if curr.task_name == task_name:
                if prev is None: # task to remove is the header
                    self.__head = curr.next
                else: # skipping over by moving the pointer to the next node
                    prev.next = curr.next
                if curr is self.__tail: # task to remove is the tailer
                    self.__tail = prev
                self.__size -= 1
                return True
            prev = curr
            curr = curr.next
        return False

    def sorted_insert_by_priority(self, head, node): # head = linkedlist, node = linkedlistnode
        current = head.__head
        previous = None
        while current:
            if current.priority < node.priority:





filepath = r'C:\Users\showm\PycharmProjects\PythonProject\.venv\Linked List\tasks.csv'

todo = Linked_List()
todo.read_tasks_from_csv(filepath)
todo.add_task('Sell', 6, 26)

print("Before remove:")
todo.display_tasks()

todo.remove_task('Sell')
print("\nAfter remove:")
todo.display_tasks()

print("\nTotal duration:", todo.calculate_total_duration())

print("\nFind Sell:", todo.find_task('Sell'))  # -> None


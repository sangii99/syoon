import csv
filepath = r'C:\Users\showm\PycharmProjects\PythonProject\.venv\Linked List\tasks.csv'
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
        with open(filepath, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            next(reader)
            for row in reader:
                task_name = row[0]
                duration = int(row[1])
                priority = int(row[2])
                self.add_task(task_name, duration, priority)


    def add_task(self, task_name, duration, priority):
        newnode = Linked_List_Node(task_name, duration, priority)
        if self.__tail == None:
            self.__head = self.__tail = newnode
        else:
            self.__tail.next = newnode
            self.__tail = self.__tail.next

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
        total_duration = 0
        tasks = read_tasks_from_csv(self, filepath)
        for task in tasks:
            duration = int(task[1])
            total_duration += duration

    def addFirst(self, node):
        newnode = Linked_List_Node(node.task_name, node.duration, node.priority)
        newnode.next = self.__head
        self.__head = newnode
        self.__size += 1
        if self.__tail is None:
            self.__tail = self.__head

    def insert(self, index, node): # index = where we insert the node, node = linkedlistnode
        if index == 0:
            self.addFirst(node)
        elif index >= self.__size:
            self.addLast(node)
        else:
            current = self.__head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Linked_List_Node(node.task_name, node.duration, node.priority)
            (current.next).next = temp
            self.__size += 1

    # put node at the very front of a (standalone) list whose head is `head`
    def _insert_front(self, head, node):
        node.next = head
        return node

    # insert `node` right after `prev` in the same list
    def _insert_after(self, prev, node):
        node.next = prev.next
        prev.next = node

    def _sorted_insert_by_priority(self, head, node):
        # case 1: empty list or node should go before current head
        if head is None or node.priority < head.priority:
            return self._insert_front(head, node)

        # case 2: find position to keep ascending priority
        current = head
        # use <= to keep stability: equal priorities stay in original relative order
        while current.next is not None and current.next.priority <= node.priority:
            current = current.next

        self._insert_after(current, node)
        return head

    def reorder_tasks_by_priority(self):
        new_head = None

        current = self.__head
        while current is not None:
            next_node = current.next  # detach first
            current.next = None
            new_head = self._sorted_insert_by_priority(new_head, current)
            current = next_node

        # replace the old list with the new sorted one
        self.__head = new_head

        # fix tail (optional but nice to have)
        tail = self.__head
        while tail and tail.next:
            tail = tail.next
        self.__tail = tail



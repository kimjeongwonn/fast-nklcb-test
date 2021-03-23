class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return not bool(self.head) or not bool(self.tail)

    def _pick_index(self, index) -> Node:
        if self.length < index:
            raise IndexError
        if self.length/2 > index:
            self.target = self.head
            while index:
                self.target = self.target.next
                index -= 1
        else:
            self.target = self.tail
            while self.length > index:
                self.target = self.target.prev
                index += 1

        return self.target

    def prepend(self, value):
        if self.is_empty():
            self.tail = self.head = Node(value, None, None)
        else:
            self.head.prev = Node(value, self.head, None)
            self.head = self.head.prev
            self.length += 1

    def append(self, value):
        if self.is_empty():
            self.tail = self.head = Node(value, None, None)
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next
            self.length += 1

    def set_head(self, index):
        self.head = self._pick_index(index)
        self.head.prev = None
        self.length -= index

    def access(self, index):
        return self._pick_index(index).value

    def insert(self, index, value):
        self.target = self._pick_index(index)
        self.temp = Node(value, self.target, self.target.prev)
        self.target.prev.next = self.temp
        self.target.prev = self.temp
        self.length += 1

    def remove(self, index):
        self.target = self._pick_index(index)
        self.target.prev.next = self.target.next
        self.target.next.prev = self.target.prev
        self.length -= 1

    def print(self):
        self.target = self.head
        self.result = []
        while self.target:
            self.result.append(self.target.value)
            self.target = self.target.next
        print(self.result)

    def print_inverse(self):
        self.target = self.tail
        self.result = []
        while self.target:
            self.result.append(self.target.value)
            self.target = self.target.prev
        print(self.result)

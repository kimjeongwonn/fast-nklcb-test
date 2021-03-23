class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return not bool(self.head)

    def _pick_index(self, index) -> Node:
        self.target = self.head
        while index:
            self.target = self.target.next
            index -= 1
        return self.target

    def _pick_termianl(self) -> Node:
        self.target = self.head
        while self.target.next:
            self.target = self.target.next
        return self.target

    def prepend(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        if self.is_empty():
            self.prepend(value)
        else:
            self._pick_termianl().next = Node(value, None)

    def set_head(self, index):
        self.head = self._pick_index(index)

    def access(self, index):
        return self._pick_index(index).value

    def insert(self, index, value):
        self.target = self._pick_index(index-1)
        self.target.next = Node(value, self.target.next)

    def remove(self, index):
        self.target = self._pick_index(index-1)
        self.target.next = self.target.next.next

    def print(self):
        self.target = self.head
        self.result = []
        while self.target:
            self.result.append(self.target.value)
            self.target = self.target.next
        print(self.result)

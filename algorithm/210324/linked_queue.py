class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, value):
        if self.head is None or self.tail is None:
            self.head = self.tail = Node(value, None, None)
            return True
        self.tail.next = Node(value, self.tail, None)
        self.tail = self.tail.next
        return True

    def get(self):
        if self.head is None or self.tail is None:
            return False
        target = self.head
        self.head = self.head.next
        target.next = None
        return target.value

    def peek(self):
        if self.head is None or self.tail is None:
            return False
        return self.head.value

    def print(self):
        result = []
        target = self.head
        while target:
            result.append(target.value)
            target = target.next
        print(result)

    def print(self):
        self.target = self.head
        if self.head is None or self.tail is None:
            self.result = '[]'
        else:
            self.result = '['
            while self.target:
                self.result += str(self.target.value)+', '
                self.target = self.target.next
            self.result = self.result[:-2] + ']'
        print(self.result)

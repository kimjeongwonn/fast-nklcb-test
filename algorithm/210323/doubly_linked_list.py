class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0  # 노드를 뒤에서 탐색하기 위해 길이를 지정

    def is_empty(self):
        # 선두노드나 말단노드가 없으면 빈 노드 (깨진 노드)
        return not bool(self.head) or not bool(self.tail)

    def __pick_index(self, index) -> Node:
        if self.length < index:  # 찾는 인덱스가 길이보다 길면 인덱스 범위 에러
            raise IndexError
        if self.length/2 > index:  # 길이의 중간보다 적으면 앞에서부터 탐색
            self.target = self.head
            while index:
                self.target = self.target.next
                index -= 1
        else:  # 그렇지 않으면 뒤에서부터 탐색
            self.target = self.tail
            while self.length > index:
                self.target = self.target.prev
                index += 1

        return self.target

    def prepend(self, value):
        if self.is_empty():  # 리스트가 비어 있다면 head와 tail에 노드 추가
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
        self.head = self.__pick_index(index)
        self.head.prev = None  # 새롭게 지정한 haed의 prev를 끊어서 끊어진 노드들을 가비지 컬렉션에 추가
        self.length -= index  # 인덱스 만큼 길이 제거

    def access(self, index):
        return self.__pick_index(index).value

    def insert(self, index, value):
        self.target = self.__pick_index(index)  # 해당 인덱스의 노드 불러오기
        # 불러온 노드의 뒷쪽에 새로운 노드를 배치
        self.temp = Node(value, self.target, self.target.prev)
        self.target.prev.next = self.temp  # 불러온 노드의 이전노드의 next를 새로운노드에 연결
        self.target.prev = self.temp  # 이전 노드를 새로운 노드로 교체
        self.length += 1

    def remove(self, index):
        self.target = self.__pick_index(index)
        self.target.prev.next = self.target.next
        self.target.next.prev = self.target.prev
        self.length -= 1

    def print(self):
        self.target = self.head
        if self.target == None:
            self.result = '[]'
        else:
            self.result = '['
        while self.target:
            self.result += str(self.target.value)+', '
            self.target = self.target.next
        self.result = self.result[:-2] + ']'
        print(self.result)

    def print_inverse(self):
        self.target = self.tail
        if self.target == None:
            self.result = '[]'
        else:
            self.result = '['
            while self.target:
                self.result += str(self.target.value)+', '
                self.target = self.target.prev
            self.result = self.result[:-2] + ']'
        print(self.result)

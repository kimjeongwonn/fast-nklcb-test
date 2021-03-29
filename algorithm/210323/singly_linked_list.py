class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return not bool(self.head)

    def __pick_index(self, index) -> Node:  # 인덱스에 해당하는 노드를 반환
        target = self.head
        while index:  # 인덱스 숫자만큼 앞으로 이동
            if target == None:  # 중간에 노드가 없으면 인덱스 범위가 벗어났으므로 에러
                raise IndexError
            target = target.next
            index -= 1
        return target

    def __pick_termianl(self) -> Node:  # 말단노드를 반환
        target = self.head
        while target.next:
            target = target.next
        return target

    def prepend(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        if self.is_empty():  # 빈 노드라면 노드 추가
            self.prepend(value)
        else:
            self.__pick_termianl().next = Node(value, None)  # 노드의 말단에 노드 추가

    def set_head(self, index):
        self.head = self.__pick_index(index)

    def access(self, index):
        return self.__pick_index(index).value

    def insert(self, index, value):
        target = self.__pick_index(index-1)  # 해당 인덱스 이전 노드를 선택
        # 새로운 노드의 next를 선택 노드의 다음 노드와 잇고 선택한 노드의 next에 배치
        target.next = Node(value, target.next)

    def remove(self, index):
        target = self.__pick_index(index-1)
        target.next = target.next.next  # 선택한 노드를 건너띄어 연결

    def print(self):
        target = self.head
        if target == None:
            self.result = '[]'
        else:
            self.result = '['
            while target:
                self.result += str(target.value)+', '
                target = target.next
            self.result = self.result[:-2] + ']'
        print(self.result)

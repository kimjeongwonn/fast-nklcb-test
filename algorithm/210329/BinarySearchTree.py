import random


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        # Ref: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/40885162
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __search(self, value):
        target = self.root
        parent = None
        direction = None

        while target:
            if target.value == value:
                break
            parent = target
            if target.value < value:
                target = target.right
                direction = 'right'
            else:
                target = target.left
                direction = 'left'
        return target, parent, direction

    def insert(self, value):
        if self.root is None:
            self.root = Node(value, None, None)
            return True
        node, parent, direction = self.__search(value)
        if node:
            return False
        if direction == 'left':
            parent.left = Node(value, None, None)
        else:
            parent.right = Node(value, None, None)
        return True

    def search(self, value):
        node, _, _ = self.__search(value)
        return node

    def remove(self, value):
        node, parent, direction = self.__search(value)
        if node == None:  # 찾은 노드가 없다면
            return False
        if node is self.root:  # 찾은 노드라 루트노드라면
            self.root = None  # 루트노드를 삭제! 이 경우 display 메서드 사용불가!
            return True
        if node.right:  # 오른쪽에 자식노드가 있다면
            target = node.right  # 오른쪽 자식노드로 이동
            target_parent = node
            while target.left:  # 오른쪽 자식노드에 왼쪽자식노드가 있다면
                target_parent = target
                target = target.left  # 좌하단의 리프노드까지 이동

            if node.left is not target:  # 삭제할 노드의 왼쪽이 자기자신이 아니라면
                target.left = node.left  # 좌하단 리프노드의 왼쪽자식에 삭제할 노드의 자식연결

            if target.right:  # 좌하단 노드의 오른쪽 자식노드가 있다면
                # 좌하단 노드의 부모노드와 좌하단 노드의 오른쪽 자식노드를 연결, 좌하단 노드는 부모와 연결해제
                target_parent.left = target.right
            else:  # 좌하단 노드의 오른쪽 자식노드가 없다면
                target_parent.left = None  # 좌하단 노드와 부모노드의 연결만 해제

            if node.right is not target:  # 삭제할 노드의 오른쪽이 자기자신이 아니라면
                target.right = node.right  # 좌하단 리프노드의 오른쪽자식에 삭제할 노드의 자식연결

            # 위 순서를 지키지 않으면 node와 target_parent가 같을경우 제대로 연결이 되지않음!

            del node  # 기존 노드 삭제 == 모든 연결 해제

            if direction == "right":  # 삭제할 노드가 오른쪽 자식이라면
                parent.right = target  # 삭제할 노드의 부모노드의 오른쪽 자식으로 좌하단 리프노드를 가져옴
            else:  # 왼쪽 자식이라면
                parent.left = target  # 삭제할 노드의 부모노드의 왼쪽 자식으로 좌하단 리프노드를 가져옴
            return True

        elif node.left:  # 오른쪽에 자식노드가 없고 왼쪽에 자식노드가 있다면 위의 로직을 방향을 바꿔서 실행하기 때문에 주석 생략
            target = node.left
            target_parent = node
            while target.right:
                target_parent = target
                target = target.right
            if node.left is not target:
                target.left = node.left
            if target.right:
                target_parent.right = target.left
            else:
                target_parent.right = None
            if node.right is not target:
                target.right = node.right
            del node
            if direction == "right":
                parent.right = target
            else:
                parent.left = target
            return True

        else:  # 리프노드인 경우
            if direction == "right":
                del node
                parent.right = None
            else:
                del node
                parent.left = None
            return True

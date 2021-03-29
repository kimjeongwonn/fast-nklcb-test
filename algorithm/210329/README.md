# BST 구현

```python
# ... remove 메서드를 제외하고 생략

    def remove(self, value):
        node, parent, direction = self.__search(value)
        if node == None:  # 찾은 노드가 없다면
            return False
        if node is self.root:  # 찾은 노드라 루트노드라면
            self.root = None # 루트노드를 삭제! 이 경우 display 메서드 사용불가!
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
                target_parent.left = target.right # 좌하단 노드의 부모노드와 좌하단 노드의 오른쪽 자식노드를 연결, 좌하단 노드는 부모와 연결해제
            else:  # 좌하단 노드의 오른쪽 자식노드가 없다면
                target_parent.left = None  # 좌하단 노드와 부모노드의 연결만 해제

            if node.right is not target: # 삭제할 노드의 오른쪽이 자기자신이 아니라면
                target.right = node.right # 좌하단 리프노드의 오른쪽자식에 삭제할 노드의 자식연결

            # 위 순서를 지키지 않으면 node와 target_parent가 같을경우 제대로 연결이 되지않음!

            del node # 기존 노드 삭제 == 모든 연결 해제

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
```

- 다 만들고 솔루션과 비교해보니, 코드가 너무 복잡했습니다. 하나씩 살펴보니 **자식이 하나만 있는 경우를 생각하지 않고 무조건 양쪽에 있을 때**를 기준으로 설계를 해서 그랬습니다.. **분기를 정확히 파악**해서 코드를 간결하게 하는 습관을 들여야한다는 것들 느꼈습니다.. 😢

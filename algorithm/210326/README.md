### 노드기반 완전이진트리 구현

```python
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, array):
        node_list = [Node(value, None, None) for value in array]
        for ind, node in enumerate(node_list):
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]

        self.root = node_list[0]

    def preorder(self):
        def recursive(node: Node):
            nonlocal result
            if node == None:
                return

            result += f'{node.value}, '
            recursive(node.left)
            recursive(node.right)

        result = "["
        recursive(self.root)
        result = result[:-2] + ']'
        print(result)

    def inorder(self):
        def recursive(node: Node):
            nonlocal result
            if node == None:
                return

            recursive(node.left)
            result += f'{node.value}, '
            recursive(node.right)

        result = "["
        recursive(self.root)
        result = result[:-2] + ']'
        print(result)

    def postorder(self):
        def recursive(node: Node):
            nonlocal result
            if node == None:
                return

            recursive(node.left)
            recursive(node.right)
            result += f'{node.value}, '

        result = "["
        recursive(self.root)
        result = result[:-2] + ']'
        print(result)

    def bfs(self, value):
        def recursive(queue):
            try:
                node = queue.pop(0)
                if node.value == value:
                    return True
            except:
                return False
            queue.append(node.left)
            queue.append(node.right)
            return recursive(queue)

        return recursive([self.root])

    def dfs(self, value):
        def recursive(node: Node):
            if node is None:
                return False
            if node.value == value:
                return True
            if recursive(node.left):
                return True
            if recursive(node.right):
                return True
            return False

        return recursive(self.root)
```

```bash
# 내 결과
[0, 1, 3, 7, 8, 4, 9, 10, 2, 5, 11, 12, 6]
[7, 3, 8, 1, 9, 4, 10, 0, 11, 5, 12, 2, 6]
[7, 8, 3, 9, 10, 4, 1, 11, 12, 5, 6, 2, 0]
False
True
True
False

# 솔루션 결과
[0 1 3 7 8 4 9 10 2 5 11 12 6 ]
[7 3 8 1 9 4 10 0 11 5 12 2 6 ]
[7 8 3 9 10 4 1 11 12 5 6 2 0 ]
False
True
True
False
```

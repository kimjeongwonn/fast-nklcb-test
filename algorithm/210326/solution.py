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
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.value == value:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

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

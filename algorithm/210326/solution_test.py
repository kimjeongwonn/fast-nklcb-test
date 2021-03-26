from solution import BinaryTree

tree = BinaryTree([i for i in range(13)])
tree.preorder()
tree.inorder()
tree.postorder()

print(tree.dfs(15))
print(tree.dfs(11))

print(tree.bfs(6))
print(tree.bfs(17))

"""Binary Tree Level Order Traversal"""
from collections import deque

# Step 1: Define Tree Node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Step 2: Level Order Traversal Function
def levelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])  # queue = [1]  first level’s first element (root node)

    while queue:
        level_size = len(queue)  #Tells how many nodes are in current level
        level = []

        for i in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


# Step 3: Create Tree Manually
# Tree:
#         7
#        / \
#       2   3
#      / \   \
#     4   5   6

root = TreeNode(7)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.right = TreeNode(6)

# Step 4: Call Function
output = levelOrder(root)

# Step 5: Print Output
print("Level Order Traversal:")
print(output)
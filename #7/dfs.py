
"""Problem: Binary Tree Maximum Path Sum"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""Tree You Want to Create

        10
       /  \
      2   10
     / \     \
    20  1     -25
               /  \
              3    4"""

# --------- BUILDING THE TREE ---------
root = TreeNode(10)

root.left = TreeNode(2)
root.right = TreeNode(10)

root.left.left = TreeNode(20)
root.left.right = TreeNode(1)

root.right.right = TreeNode(5)
root.right.right.left = TreeNode(3)
root.right.right.right = TreeNode(4)


# --------- SOLUTION ---------
class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            current_sum = node.val + left + right
            self.max_sum = max(self.max_sum, current_sum)
            
            return node.val + max(left, right)
        
        dfs(root)
        return self.max_sum


# --------- RUN ---------
sol = Solution()
print(sol.maxPathSum(root))   # Output: 42
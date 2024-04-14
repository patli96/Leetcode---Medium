# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        left_leaves_sum = 0
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if node.left is not None:
                if node.left.left is None and node.left.right is None:
                    left_leaves_sum += node.left.val
                else:
                    stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return left_leaves_sum


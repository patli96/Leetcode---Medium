# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        if not preorder:
            return []

        # construct BST
        root = TreeNode(preorder[0], None, None)

        if len(preorder) == 1:
            return root

        def construct_BST(root, num):
            if num < root.val:
                if root.left is not None:
                    construct_BST(root.left, num)
                else:
                    root.left = TreeNode(num, None, None)
            else:
                if root.right is not None:
                    construct_BST(root.right, num)
                else:
                    root.right = TreeNode(num, None, None)

        for i in range(1, len(preorder)):
            construct_BST(root, preorder[i])

        return root
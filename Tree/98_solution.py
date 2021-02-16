# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        if not root:
            return False

        def inorderTraversal(root):
            '''
            generate a list of node's values by inorder traversal
            '''
            res = []
            if root:
                res = inorderTraversal(root.left)
                res.append(root.val)
                res = res + inorderTraversal(root.right)
            return res

        inorder_list = inorderTraversal(root)

        # if the values in the list are not strictly ascending then return FALSE
        for i in range(len(inorder_list) - 1):
            if inorder_list[i + 1] <= inorder_list[i]:
                return False

        return True
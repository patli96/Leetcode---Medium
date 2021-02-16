# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def successor(self, root):
        '''
        Find the smallest node after the current one.
        One step right, and go left as far as you can.
        '''
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        '''
        Find the largest node before the current one.
        One step left, and go right as far as you can.
        '''
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        if not root:
            return None

        # find the node with a value of the given key
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the node if it is found
        else:
            # if the node is a leaf
            if not root.left and not root.right:
                root = None
            # if the node has a right child
            # --> replace it with its successor and recursively delete the successor in the right subtree
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # if the node only has a left child
            # --> replace it with its predecessor and recursively delete the predecessor in the left subtree
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root

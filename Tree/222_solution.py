# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        queue = collections.deque([root])
        steps = 0

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == 0 and node.left is None:
                    print(f'size = {size}, steps = {steps}')
                    return 2 ** (steps) - 1 + size
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            steps += 1

        return None
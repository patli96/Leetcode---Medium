"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root or (root.left is None and root.right is None):
            return root

        # implement a BFS to traverse the tree
        queue = [root, 0]

        while len(queue) != 0:
            # use a list to store nodes at the next level
            next_level = []
            # traverse the current queue to link nodes at the same level
            for i in range(1, len(queue)):
                if queue[i] != 0:
                    queue[i - 1].next = queue[i]
                    if queue[i - 1].left is not None:
                        next_level.append(queue[i - 1].left)
                        next_level.append(queue[i - 1].right)
                else:
                    if queue[i - 1].left is not None:
                        next_level.append(queue[i - 1].left)
                        next_level.append(queue[i - 1].right)
                    if len(next_level) != 0:
                        next_level.append(0)
            queue.clear()
            queue += next_level

        return root
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
        queue = []
        queue.append(root)
        while len(queue) > 0:
            new_queue = []
            for i in range(len(queue) - 1):
                queue[i].next = queue[i + 1]
                node = queue[i]
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            if queue[-1]:
                if queue[-1].left:
                    new_queue.append(queue[-1].left)
                if queue[-1].right:
                    new_queue.append(queue[-1].right)
            queue = new_queue
        return root


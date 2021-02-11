"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if head is None:
            return head

        # use a dictionary to record each original node and its deep copy
        node_hash_map = {}

        # a function to clone a node's next node
        def cloneNext(old):
            # if the next node is already in the dictionary
            if old.next is not None and old.next in node_hash_map:
                new_node.next = node_hash_map[old.next]
            # if the next node is not in the dictionary
            elif old.next is not None:
                new_next = Node(old.next.val, None, None)
                node_hash_map[old.next] = new_next
                new_node.next = new_next
            # if the next node is None
            else:
                new_node.next = None

        # a function to clone a node's random node
        def cloneRandom(old):
            # if the random node is already in the dictionary
            if old.random is not None and old.random in node_hash_map:
                new_node.random = node_hash_map[old.random]
            # if the random node is not in the dictionary
            elif old.random is not None:
                new_random = Node(old.random.val, None, None)
                node_hash_map[old.random] = new_random
                new_node.random = new_random
            # if the random node is None
            else:
                new_node.random = None

        old = head
        new_head = Node(old.val, None, None)

        node_hash_map[head] = new_head

        # traverse the original linked list and deep copy it node by node
        while old is not None:
            if old in node_hash_map:
                new_node = node_hash_map[old]
            else:
                new_node = Node(old.val, None, None)
                node_hash_map[old] = new_node
            cloneNext(old)
            cloneRandom(old)
            old = old.next

        return new_head

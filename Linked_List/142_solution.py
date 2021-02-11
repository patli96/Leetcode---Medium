# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        if head is None:
            return None

        # use a dictonary to record visited node and its index
        idx_dict = {}
        idx = 0
        ptr = head

        # traverse the linked list
        while ptr is not None:
            # if a node is already in the dictonary, then it's the beginning of the cycle
            if ptr in idx_dict:
                return ptr
            idx_dict[ptr] = idx
            ptr = ptr.next
            idx += 1

        return None


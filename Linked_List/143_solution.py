# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if head is not None:

            # use a dictionary to record each node and its index
            idx_dict = {}
            idx = 0
            ptr = head

            # traverse the linked list to record each node and its index
            while ptr is not None:
                idx_dict[idx] = ptr
                ptr = ptr.next
                idx += 1

            # n is the last index number
            n = idx - 1
            # m is the index of the middle node of the linked list
            if n % 2 == 0:
                m = int(n / 2)
            else:
                m = int((n - 1) / 2)

            # use a for-loop to reconnect the linked list, in the order of node[i] -> node[n-i]
            for i in range(m):
                print(f'm = {m}\t{idx_dict[i].val}->{idx_dict[n - m].val}->{idx_dict[i + 1].val}')
                idx_dict[i].next = idx_dict[n - i]
                idx_dict[n - i].next = idx_dict[i + 1]

            # set the last node's next to None
            if n % 2 == 0:
                idx_dict[m].next = None
            else:
                idx_dict[m + 1].next = None


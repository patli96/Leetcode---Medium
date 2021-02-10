# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if head is None or head.next is None:
            return head

        # if the first a few nodes are duplicate
        while head.val == head.next.val:
            new_head = head.next
            while new_head is not None and new_head.val == head.val:
                new_head = new_head.next
            if new_head is None:
                return None
            if new_head.next is None:
                return new_head
            head = new_head

        # use two pointers to traverse the whole linked list
        curr = head
        next = curr.next

        while next.next is not None:
            next_next = next.next
            # if find duplicate nodes
            if next.val == next_next.val:
                while next_next is not None and next.val == next_next.val:
                    next_next = next_next.next
                if next_next is None:
                    curr.next = None
                    return head
                if next_next.next is None:
                    curr.next = next_next
                    return head
                curr.next = next_next
                next = next_next
            else:
                curr = curr.next
                next = next.next

        return head

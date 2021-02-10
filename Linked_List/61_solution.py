# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if head is None or head.next is None:
            return head

        list_len = 1
        ptr = head
        while ptr.next is not None:
            ptr = ptr.next
            list_len += 1

        list_end = ptr
        k = k % list_len
        if k == 0:
            return head
        target = list_len - k

        ptr = head
        count = 1
        while count < target:
            ptr = ptr.next
            count += 1
        new_head = ptr.next
        ptr.next = None
        list_end.next = head
        return new_head
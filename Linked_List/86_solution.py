# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        if head is None or head.next is None:
            return head

        # initialize two dummy heads
        before_head = ListNode()
        after_head = ListNode()

        # initialize two pointers to add new nodes to each linked list
        before = before_head
        after = after_head

        ptr = head

        # traverse the given linked list and add each node to different linked list based on their values
        while ptr is not None:
            if ptr.val < x:
                next = ptr.next
                before.next = ptr
                ptr.next = None
                ptr = next
                before = before.next
            else:
                next = ptr.next
                after.next = ptr
                ptr.next = None
                ptr = next
                after = after.next

        # concatenate two linked lists
        if before_head.next is None:
            head = after_head.next
        else:
            head = before_head.next

        before.next = after_head.next

        return head
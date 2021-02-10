# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if not head or head.next is None or m == n:
            return head

        ptr = head

        a, b, c, d = None, None, None, None

        len_list = 0

        while ptr is not None:
            len_list += 1
            # print(f'No.{len_list}: {ptr.val}')

            if len_list == m - 1:
                a = ptr
            elif len_list == m:
                b = ptr
                curr = ptr
                pre = None
                while len_list <= n:
                    # print(f'current node: {curr.val}, len_list = {len_list}')
                    next = curr.next
                    curr.next = pre
                    pre = curr
                    curr = next
                    len_list += 1
                d = curr
                c = pre
                # print([a, b, c ,d])
                if a is None and d is None:
                    return c
                elif a is None and d is not None:
                    b.next = d
                    return c
                elif a is not None and d is None:
                    a.next = c
                    return head
                else:
                    a.next = c
                    b.next = d
                    return head

            ptr = ptr.next

        return head
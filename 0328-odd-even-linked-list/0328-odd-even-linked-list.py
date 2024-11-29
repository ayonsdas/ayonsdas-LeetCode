# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = ListNode(0, None)
        b = ListNode(0, None)
        c = a
        d = b
        i = 1
        while head:
            x = head
            head = head.next
            x.next = None
            if i % 2:
                c.next = x
                c = c.next
            else:
                d.next = x
                d = d.next
            i = 1 - i
        c.next = b.next
        return a.next
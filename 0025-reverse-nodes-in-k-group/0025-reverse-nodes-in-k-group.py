# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        t = head
        c = 0
        while t:
            t = t.next
            c += 1
        t = ListNode(0, None)
        b = t
        x = head
        d = c
        while d > (c - math.floor(c / k) * k):
            a = x
            x = x.next
            if (c - d) % k == 0:
                while b.next:
                    b = b.next
            a.next = b.next
            b.next = a
            d -= 1
        while b.next:
            b = b.next
        while x:
            a = x
            x = x.next
            a.next = None
            b.next = a
            b = b.next
        return t.next
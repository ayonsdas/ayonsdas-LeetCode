# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        track = 1
        t = ListNode(0, None)
        x = head
        b = t
        while x:
            a = x
            x = x.next
            a.next = None
            if track < left or track > right:
                while b.next:
                    b = b.next
                b.next = a
                b = b.next
            else:
                a.next = b.next
                b.next = a
            track += 1
        return t.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        t = head
        c = 0
        while t:
            c += 1
            t = t.next
        k %= c
        if k == 0:
            return head
        t = head
        p = None
        for i in range(c - k):
            p = t
            t = t.next
        p.next = None
        l = t
        while l.next != None:
            l = l.next
        l.next = head
        return t
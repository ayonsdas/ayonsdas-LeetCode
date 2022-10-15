# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = 0
        t = head
        while t:
            t = t.next
            l += 1
        a = b = head
        for i in range(k - 1):
            a = a.next
        for i in range(l - k):
            b = b.next
        a.val, b.val = b.val, a.val
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = 0
        t = head
        while t:
            t = t.next
            x += 1
        if x < 2:
            return None
        p = None
        l = head
        for i in range(x // 2):
            p = l
            l = l.next
        p.next = l.next
        return head
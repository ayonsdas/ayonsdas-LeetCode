# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        s = f = head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
            if s == f:
                break
        else:
            return None
        while head != s:
            head, s = head.next, s.next
        return s
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        if not head:
            return None
        while head.next:
            b = head
            head = head.next
            if b in s:
                return b
            s.add(b)
        return None
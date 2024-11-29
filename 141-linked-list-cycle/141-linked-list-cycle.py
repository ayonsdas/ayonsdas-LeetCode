# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return False
        
        f = head
        s = head
        
        while f and f.next:
            f = f.next.next
            s = s.next
            if f == s:
                return True
            
        return False
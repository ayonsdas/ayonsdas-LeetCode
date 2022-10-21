# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        def b(r: ListNode) -> int:
            if not r.next:
                r.val += 1
                if r.val == 10:
                    r.val = 0
                    return 1
                else:
                    return 0
            r.val += b(r.next)
            if r.val == 10:
                r.val = 0
                return 1
            return 0
        b(head)
        if head.val == 0:
            head = ListNode(1, head)
        return head
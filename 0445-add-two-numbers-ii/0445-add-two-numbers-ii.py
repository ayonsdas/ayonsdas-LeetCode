# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = j = 0
        a1 = l1
        a2 = l2
        while a1:
            i *= 10
            i += a1.val
            a1 = a1.next
        while a2:
            j *= 10
            j += a2.val
            a2 = a2.next
        k = str(i + j)
        t = ListNode(0, None)
        x = t
        for char in k:
            x.next = ListNode(int(char), None)
            x = x.next
        return t.next
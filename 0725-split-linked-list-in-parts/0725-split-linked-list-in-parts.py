# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        t = 0
        x = head
        while x:
            t += 1
            x = x.next
        a, b = t // k, t % k
        c = []
        i = 0
        j = 0
        x = head
        y = x
        while y:
            l = y
            y = y.next
            j += 1
            if j == a + (1 if i < b else 0):
                j = 0
                i += 1
                l.next = None
                c.append(x)
                x = y
        while len(c) < k:
            c.append(None)
        return c
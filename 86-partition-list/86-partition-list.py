# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        saved = []
        saved2 = []
        while head != None:
            if head.val < x:
                saved.append(head.val)
            else:
                saved2.append(head.val)
            head = head.next
        newHead = ListNode(0, None)
        t = newHead
        for i in range(len(saved)):
            t.next = ListNode(saved[i], None)
            t = t.next
        for i in range(len(saved2)):
            t.next = ListNode(saved2[i], None)
            t = t.next
        return newHead.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = []
        temp = temp2 = head
        while temp2 and temp2.next:
            temp = temp.next
            temp2 = temp2.next.next
        head2 = ListNode(0, None)
        while temp:
            x = temp.next
            temp.next = head2.next
            head2.next = temp
            temp = x
        head2 = head2.next
        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True
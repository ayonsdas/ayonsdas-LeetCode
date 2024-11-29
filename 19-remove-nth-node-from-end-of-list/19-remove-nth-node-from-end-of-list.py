# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 1
        while temp.next != None:
            count += 1
            temp = temp.next
        main = ListNode(5, None)
        tempTrav = head
        temp = main
        while count > 1:
            if count != n:
                temp.next = ListNode(tempTrav.val, None)
                tempTrav = tempTrav.next
                temp = temp.next
            else:
                tempTrav = tempTrav.next
            count -= 1
        if n != 1:
            temp.next = ListNode(tempTrav.val, None)
        return main.next
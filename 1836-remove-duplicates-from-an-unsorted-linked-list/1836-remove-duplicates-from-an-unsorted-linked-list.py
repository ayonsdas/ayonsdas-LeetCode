# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        
        one = set()
        two = set()
        
        temp = head
        while temp:
            if not temp.val in one:
                one.add(temp.val)
            else:
                two.add(temp.val)
            temp = temp.next
        r = ListNode(0, None)
        x = r
        temp = head
        while temp:
            if not temp.val in two:
                x.next = ListNode(temp.val, None)
                x = x.next
            temp = temp.next
                
        return r.next
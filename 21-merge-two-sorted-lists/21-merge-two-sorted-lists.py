# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)
        t = head
        while list1 or list2:
            if not list1:
                t.next = ListNode(list2.val, None)
                list2 = list2.next
            elif not list2:
                t.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                if list1.val < list2.val:
                    t.next = ListNode(list1.val, None)
                    list1 = list1.next
                else:
                    t.next = ListNode(list2.val, None)
                    list2 = list2.next
            t = t.next
        return head.next
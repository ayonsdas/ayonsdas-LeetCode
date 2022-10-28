/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */

class Solution {
    fun hasCycle(head: ListNode?): Boolean {
        var f = head;
        var s = head;
        while(f != null && f.next != null && s != null)
        {
            f = f.next.next;
            s = s.next;
            if(f == s)
            {
                return true;
            }
        }
        return false;
    }
}
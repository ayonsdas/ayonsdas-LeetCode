/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution {

    /**
     * @param ListNode $head
     * @return ListNode
     */
    function deleteDuplicates($head) {
        $temp = $head;
        while($temp != null)
        {
            if($temp->next == null)
            {
                break;
            }
            if($temp->val == $temp->next->val)
            {
                $temp->next = $temp->next->next;
            }
            else
            {
                $temp = $temp->next;
            }
        }
        return $head;
    }
}

/**
ListNode* temp = head;
        while(temp != nullptr)
        {
            if(temp->next == nullptr)
                break;
            if(temp->val == temp->next->val)
                temp->next = temp->next->next;
            else
                temp = temp->next;
        }
        return head;*/
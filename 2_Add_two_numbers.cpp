/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* result = new ListNode();
        auto listIterator = result;
        int carry = 0;
        while(l1 != nullptr || l2 != nullptr){
            int x = (l1 != nullptr)?l1->val:0;
            int y = (l2 != nullptr)?l2->val:0;
            
            int sum = x + y + carry;
            int remainder = sum % 10;
            carry = sum / 10;
            
            listIterator->next = new ListNode(remainder);
            listIterator = listIterator->next;
            
            if(l1 != nullptr){
                l1 = l1->next;
            }
            if(l2 != nullptr){
                l2 = l2->next;
            }
        }
        if(carry){
            listIterator->next = new ListNode(carry);
        }
        return result->next;
    }

};
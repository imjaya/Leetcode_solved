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
    ListNode* removeNthFromEnd(ListNode* head, int k) {
        if(!head || !head->next)return NULL;
        ListNode dummy(0), *cur = &dummy;
        cur->next = head;
        ListNode* former = cur, *latter = cur;
        while(k){
            latter = latter->next;
            k--;
        }
        while(latter && latter->next){
            former = former->next;
            latter = latter->next;
        }
        former->next = former->next->next; // ? former->next->next : NULL;
        return dummy.next;
    }
};
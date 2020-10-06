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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* newHead = new ListNode(0, head);
        ListNode* newTemp = newHead;
        ListNode* DuplicateTemp = newHead;


        while(DuplicateTemp && DuplicateTemp->next){
    
            DuplicateTemp = DuplicateTemp->next;
            
            while((DuplicateTemp && DuplicateTemp->next) && DuplicateTemp->val == DuplicateTemp->next->val){
                DuplicateTemp = DuplicateTemp->next;
                
                if(DuplicateTemp->next == NULL || DuplicateTemp->val != DuplicateTemp->next->val)
                    DuplicateTemp = DuplicateTemp->next;
            }
            
            newTemp->next = DuplicateTemp;
            newTemp = newTemp->next;
        }
        
        return newHead->next;
    }
};
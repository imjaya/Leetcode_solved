class Solution { public: ListNode* reverseList(ListNode* head) {
        if (head == NULL) 
            return NULL; 
        if (head->next == NULL) 
            return head; 
        
        ListNode *curr = head; 
        ListNode *prev = NULL; 
        
        while (curr) { 
            head = curr->next; 
            curr->next = prev; 
            prev = curr; 
            curr = head; 
        } 
        return prev; 
    }
};
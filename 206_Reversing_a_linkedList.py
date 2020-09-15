# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev=None
        
        while(head!= None):
            next_node=head.next
            head.next=prev
            prev=head
            head=next_node
            
            
        return prev

############################################################################

class Solution:
    
    def helper(self, prev, cur):
        
        if cur:

            # locate next hopping node
            next_hop = cur.next
            
            # reverse direction
            cur.next = prev
        
            return self.helper( cur, next_hop)
        
        else:

            # new head of reverse linked list
            return prev    
            
    
    def reverseList(self, head: ListNode) -> ListNode:
        
        return self.helper( None, head)
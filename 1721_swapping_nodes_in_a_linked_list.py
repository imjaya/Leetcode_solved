from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Find the kth node from the beginning of the list
        temp1 = temp2 = head
        for i in range(k-1):
            temp1 = temp1.next
        k_node = temp1

        # Step 2: Find the Kth node from the end, which is nothing but N-K+1,
        # I acheive this by moving the head pointer(temp2), unitil the pointer
        # pointing at Kth node reaches the end.
        while temp1.next:
            temp2 = temp2.next
            temp1 = temp1.next
        
        temp2.val, k_node.val = k_node.val, temp2.val
        return head
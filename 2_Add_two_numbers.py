# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = temp = ListNode(0)
        remainder = 0
        while l1 or l2:
            totalVal = 0
            if l1:
                totalVal += l1.val
                l1 = l1.next  
            if l2:
                totalVal += l2.val
                l2 = l2.next
           
            (remainder,val) = divmod(totalVal+remainder, 10)
            temp.next = ListNode(val)
            temp = temp.next
        
        if remainder > 0:
            temp.next = ListNode(remainder)
        
        return head.next
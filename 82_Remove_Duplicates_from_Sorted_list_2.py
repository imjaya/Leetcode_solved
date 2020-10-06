# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans = ListNode()
        res = ans
        while head:
            if head.next and head.val != head.next.val: # if adjacent elements are not same append to res
                ans.next = ListNode(head.val)
                ans = ans.next
                head = head.next
            elif head.next and head.val == head.next.val: # if  adjacent elements are same, skip the current till current head value is skipped
                skip = head.val
                while head and skip == head.val:
                    head = head.next
            else:
                ans.next = ListNode(head.val)
                ans = ans.next
                head = head.next
        
        return res.next
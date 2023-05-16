from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        temp = result = head
        swap = True
        while head.next:
            head = head.next
            val = temp.val
            if swap:
                swap = False
                temp.val = head.val
                head.val = val
            else:
                swap = True
            temp = temp.next
        return result
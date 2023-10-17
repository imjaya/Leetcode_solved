# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dumy = ListNode()
        dumy.next = head
        first = dumy
        second = dumy
        for i in range(0,n+1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dumy.next
    

# Two pass solution TC: O(2*N), SC: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        temp1 = head
        while temp1:
            temp1 = temp1.next
            size += 1
        remove_index = size - n + 1
        temp1 = head
        cur_index=1
        if remove_index == 1:
            return head.next
        while temp1:
            if remove_index == cur_index+1:
                temp1.next=temp1.next.next if temp1.next else None
                break
            temp1 = temp1.next
            cur_index+=1

        return head
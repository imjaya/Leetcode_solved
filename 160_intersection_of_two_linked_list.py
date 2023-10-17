# Has set approach TC: O(N+M) SC: O(M)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        while headB:
            visited.add(headB)
            headB = headB.next

        while headA:
            if headA in visited:
                return headA
            headA = headA.next
        
        return None
    
# Pytohn two pointer approach TC: O(N+M), SC: O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB

        while(p1 !=p2):
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
#two pointer approach, one fast pointer and one slow pointer
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Floyd Cycle Detection Algorithm, Tortoise and Hare Algorithm, Fast and slow pointers
        walker,runner = head,head
        #runner = head
        while runner != None and runner.next != None:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        return False
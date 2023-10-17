#Greedy Solution TC: O(log(n)), SC: O(log(n))
import math
class Solution:
    def minOperations(self, n: int) -> int:

        d = math.floor(math.log(n, 2))
        if n == pow(2, d):
            return 1
        
        low = pow(2, d)
        high = pow(2, d+1)
        return 1 + min(self.minOperations(n-low), self.minOperations(high-n))

        
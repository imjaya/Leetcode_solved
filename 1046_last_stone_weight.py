#brute force solution TC: O(N*N), SC: O(!)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        def get_largest_elem():
            pos = stones.index(max(stones))
            stones[pos], stones[-1] = stones[-1], stones[pos]
            return stones.pop()

        while len(stones) > 1:
            largest_1 = get_largest_elem()
            largest_2 = get_largest_elem()
            if largest_1 != largest_2:
                stones.append(largest_1-largest_2)
        return stones[-1] if stones else 0

#optimal solution using heapq TC: O(N*log(N)) , SC:O(1)
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range (0, len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)

        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if a != b:
                heapq.heappush(stones, a-b)
        return -1*heapq.heappop(stones) if len(stones) else 0

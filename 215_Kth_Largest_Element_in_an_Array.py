class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        result=0
        for num in nums:
            heapq.heappush(heap, -num)
        for i in range(k):
            result=heapq.heappop(heap)
        return -1*result
        
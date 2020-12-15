#form a dictionary structure and then heapify the dict as a tuple with neagtive if count value and pop the k number of elements
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = [] # Space O(N)
        counter=collections.Counter(words)
        for word, count in counter.items(): # M: num of words w/o duplicate Time O(M*logM)
            heapq.heappush(heap, (-count, word))
        res = []
        for i in range(k): # Time O(k*logM)
            count, word = heapq.heappop(heap)
            res.append(word)
        return res
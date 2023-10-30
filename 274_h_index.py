# sort in reverse and check from which position the citations are less than the posiiton index
# TC: O(NLogN) SC: O(1)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0

        for i in range(0, len(citations)):
            if i < citations[i]:
                h_index += 1
            else:
                break
        return h_index
    

# Counting sort approach.
#TC: O(N) SC: O(1)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #counting sort make count array
        n = len(citations)
        count_array = [0] * (n + 1)
        for citation in citations:
            count_array[min(n, citation)] += 1

        count = 0
        for k in range(len(count_array) - 1, -1, -1):
            count += count_array[k]
            if count >= k:
                return k
        return 0


        

        
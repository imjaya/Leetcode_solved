class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        result = 0
        start = arrays[0][0]
        end = arrays[0][len(arrays[0]) - 1]
        
        for i in range(1, len(arrays)):
            result = max(result, max(abs(arrays[i][len(arrays[i]) - 1] - start), abs(end - arrays[i][0])))
            start = min(start, arrays[i][0])
            end = max(end, arrays[i][len(arrays[i]) - 1])
        
        return result
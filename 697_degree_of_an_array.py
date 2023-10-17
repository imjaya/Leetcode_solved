class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count, min_i, max_i = {}, {}, {}
        for i in range(0, len(nums)):
            if nums[i] not in count: 
                min_i[nums[i]] = i
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
            max_i[nums[i]] = i

        degree = max(count.values())
        print(degree, count, min_i, max_i)
        result = []
        for k,v in count.items():
            if v == degree:
                result.append(max_i[k] - min_i[k]+1)
        return min(result)
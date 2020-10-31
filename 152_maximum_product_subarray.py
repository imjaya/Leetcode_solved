#max product similar to max sum order of N
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        best = nums[0]
        imax, imin = nums[0], nums[0]
        for num in nums[1:]:
            cand = [num, imax*num, imin*num]
            imax = max(cand)
            imin = min(cand)
            best = max([best, imax, imin])
            
        return best
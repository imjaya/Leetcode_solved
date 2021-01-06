class Solution:
    def specialArray(self, nums: List[int]) -> int:
        #
        for i in range(1,101):
            if sum(ele>=i for ele in nums) == i:
                return i
        return -1

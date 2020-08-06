class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        max_num=len(nums)
        min_num=min(nums)
        expected_sum=0
        for i in range(min_num,max_num+1):
            expected_sum+=i
        actual_sum=sum(nums)
        
        return(expected_sum-actual_sum)
        
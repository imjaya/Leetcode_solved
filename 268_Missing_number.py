#finding the missing number in a consecutive set of numbers
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        max_num=len(nums)
        min_num=min(nums)
        expected_sum=0
        for i in range(min_num,max_num+1):
            expected_sum+=i
        actual_sum=sum(nums)
        
        return(expected_sum-actual_sum)
    
# XOR Approach TC: O(2N) SC: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^=num
        for i in range(0, len(nums)+1):
            result ^= i
        return result
    
# Total Sum Approach TC: O(N) SC(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = n*(n+1)/2

        for num in nums:
            result -= num
        return result


        
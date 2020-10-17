#O(N^2) to outpur all the sbsets of array
class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n=len(nums)
        output=[[]]
        for num in nums:
            output+=[curr+[num]for curr in output]
            print(output)
        return(output)
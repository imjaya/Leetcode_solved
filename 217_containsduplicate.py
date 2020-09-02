class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        L=set(nums)
        if(len(L)<len(nums)):
            return(True)
        return(False)
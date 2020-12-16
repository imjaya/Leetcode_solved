class Solution:
    def helper(self,nums,tmp):
        if len(tmp) == self.nums_len:
            self.result.append(tmp)
            return
        for i in range(len(nums)):
            self.helper(nums[:i]+nums[i+1:],tmp+[nums[i]])
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.nums_len = len(nums)
        self.helper(nums,[])
        return self.result
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num={}
        
        for i in nums:
            if i not in num:
                num[i]=1
            else:
                num[i]+=1
                
        for i in num:
            if(num[i]>len(nums)/2):
                return(i)
        
#Approach1 Brute Force (wrong approach)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return(nums[0])
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)-1):
                if(nums[j]<nums[i]):
                    return(nums[j])
        return(min(nums))
#Approach2 Binary search
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if(len(nums)==1):
            return(nums[0])
                
        l=0
        r=len(nums)-1
        if(nums[r]>nums[l]):
            return(nums[l])
        
        while(l<=r):
            mid=(l+r)//2
            
            if(nums[mid]>nums[mid+1]):
                return(nums[mid+1])
            if(nums[mid-1]>nums[mid]):
                return(nums[mid])
            if(nums[mid]>nums[l]):
                l=mid+1
            else:
                r=mid-1
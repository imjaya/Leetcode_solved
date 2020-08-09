class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        s=0
        minn=6000
        if(len(nums)==3):
            return(sum(nums))
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if(nums[i]+nums[j]+nums[k]==target):
                        return(target)
                    else:
                        s=nums[i]+nums[j]+nums[k]
                        if(abs(target - s) < abs(target - minn)):
                            minn=s
                            
        return(minn)
        
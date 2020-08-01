class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []
#         R=nums.copy()
#         nums.sort()
#         low,high=0,len(nums)-1
        
#         while(low<high):
#             if(nums[low]+nums[high]==target):
#                 L.append(R.index(nums[low]))
#                 L.append(R.index(nums[high]))
#                 break
#             elif(nums[low]+nums[high]<target):
#                 low=low+1
#             else:
#                 high=high-1
        
        # for i in range(0,len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if(nums[i]+nums[j]==target):
        #             L.append(i)
        #             L.append(j)
        #             break
        
        
        #return L
            
        
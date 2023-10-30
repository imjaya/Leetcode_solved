# Hashmap approach TC: O(N) SC: O(N), 
#another approach could sorting and then determine the element in the N//2 +1 position TC: O(NlonN) SC: O(1)
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
            
# Boyer Moore Voting Algorithm TC: O(N) SC: O(1), 
# since its abut majority its all abouot finding who is the max occuring elemtent until the current vote (till current element), 
# cancel out (-1) when youo see any other elemtent which was not the max occuring elemtent until now.
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
            

        
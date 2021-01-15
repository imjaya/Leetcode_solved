class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        
        missing=[]
        hash_table={}
        for num in nums:
            if(num not in hash_table):
                hash_table[num]=1
            else:
                hash_table[num]+=1
            
        for i in range(1,len(nums)+1):
            if(i not in hash_table):
                missing.append(i)
        return(missing)
        
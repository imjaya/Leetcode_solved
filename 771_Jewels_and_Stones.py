class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_dict=defaultdict(int)
        for i in jewels:
            jewels_dict[i]+=1
        # print(jewels_dict)
        count=0
        for i in stones:
            if i in jewels_dict:
                count+=1
        return count
        
        
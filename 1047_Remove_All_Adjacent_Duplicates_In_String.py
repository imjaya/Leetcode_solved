class Solution:
    def removeDuplicates(self, S: str) -> str:
        result=[]
        for i in range(0,len(S)):
            # print(result)
            if(result and S[i]==result[-1]):
                result.pop(-1)
            
            else:
                result.append(S[i])
        return ("").join(result)
            
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}
        for i in strs:
            A=sorted(str(i))
            if not result or (str(A) not in result.keys()):
                result[str(A)]=[str(i)]
            elif(str(A) in result.keys()):
                result[str(A)].append(str(i))
            else:
                continue
        result_1=[]
        for i in result.values():
            result_1.append(i)
        return(result_1)
        
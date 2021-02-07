class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        
        p=0
        if(len(s)==0):
            return True
        for i in range(0,len(t)):
            if(t[i]==s[p]):
                p+=1
            if(p==len(s)):
                return True
        return False
            
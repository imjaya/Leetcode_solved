def helper(s,l,r):
        while l<r:
            if(s[l]!=s[r]):
                return False
            l+=1
            r-=1
        return True
class Solution:  
        

    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while(left<right):
            if(s[left]!=s[right]):
                return helper(s,left+1,right) or helper(s,left,right-1)
            else:
                left+=1
                right-=1
        return True
        
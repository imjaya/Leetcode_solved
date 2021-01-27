class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        R=""
        for i in range(len(s)):
            if(s[i] in alphanumeric):
                R+=s[i].lower()
        print(R)
        
        i=0
        j=len(R)-1
        while(i<=j):
            if(R[i] !=R[j]):
                return False
            i+=1
            j-=1
            
        return True
        
            
        
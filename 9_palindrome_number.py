#palindrome check
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0 or (x!=0 and x%10==0)):
            return False
        rever=0
        while(x>rever):
            rever=rever*10+(x%10)
            x=x//10
        if(x==rever or x==rever//10):
            return True
        else:
            return False
        
        
        
        
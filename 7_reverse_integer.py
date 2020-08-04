class Solution:
    def reverse(self, x: int) -> int:
        
        flag=0
        if(x<0):
            flag=1
            x=x*(-1)
        
        p=0
        r=1
        while(x>0):
            r=x%10
            p=p*10+r
            x=x//10
        if((p>2**31-1) or (-p<-2**31)):
            return(0)
        if(flag==1):
            return(-p)
        return(p)
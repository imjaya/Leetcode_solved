def convert(a,n):
    r={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
    i=0
    ans=0
    while(n>0):
        ans+=r[a[i]]*(10**(n-1))
        # print(ans,n,r[a[i]])
        n=n-1
        i=i+1
    # print(ans)
    return ans
class Solution:
   
            
    def multiply(self, num1: str, num2: str) -> str:
        
        return(str(convert(num1,len(num1))*convert(num2,len(num2))))
        
#include <cmath>
class Solution {
public:
    int reverse(long long x) {
        int flag=0;
        if(x<0){
        x=x*-1;
        flag=1;
        
        }
        long long result=0;
        int remainder=0;
        
        while(x>0)
        {
        remainder=x%10;
        result=result*10 +remainder;
        x=x/10;
            
        
        }
        if((result> std::pow(2,31)-1) || (-result <std::pow(-2,31)))
        {
        return(0);
        }
        
        if(flag==1)
        {
        return(-result);
        
        }
        
        return(result);
        
        
    }
};
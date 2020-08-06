class Solution {
public: 
   
    string intToRoman(int num) {
        string letter[]={"I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"};
        int value[]= {1,4,5,9,10,40,50,90,100,400,500,900,1000};
        string ans;
        while(num)
        {
            for(int i=12;i>=0;i--)
            {
                int q=num/value[i];
                if(q)
                {
                    while(q--)
                        ans+=letter[i];
                    num%=value[i];
                    break;
                }
            }   
        }
        return ans;
    }
};
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        for (int i=0;i<n;i++)
        {
            int index=n-i-1;
            if(digits[index]==9)
            {
                digits[index]=0;
            }
            else
            {
                digits[index]+=1;
                    return(digits);
            }
        }
        digits.insert(digits.begin(),1); 
        return(digits);
    }
};
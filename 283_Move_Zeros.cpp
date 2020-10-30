class Solution {
public:
    void moveZeroes(vector<int>& nums) {
    int numZeroes = 0;
    for (int i = 0; i < nums.size(); i++) {
        numZeroes += (nums[i] == 0);
    } 
        int i=0, j=0;
     while (i<nums.size() && j<nums.size()) {
        if (nums[j]!=0)
        {swap (nums[i], nums[j]); i++;}
        j++;
    }
   while (numZeroes) {
        nums[nums.size()-numZeroes]=0;
       numZeroes--;
        }  
    }
};
class Solution {
public:
    int specialArray(vector<int>& nums) {
        
        sort(nums.rbegin(),nums.rend());
        
        for(int i=0; i<nums.size()-1; )
            if(++i<=nums[i-1] and i>nums[i]) return i;
        
        return nums.size()<=nums[nums.size()-1]?nums.size():-1;
    }
};
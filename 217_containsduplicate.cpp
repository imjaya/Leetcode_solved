class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, int> freq;
        int i = 0;
        int n = nums.size();
        while (i < n){
            freq[nums[i]] +=1;
            i++;
        }
        bool res = false;
        map<int, int>::iterator it = freq.begin();
        for(; it != freq.end(); it ++){
            if (it->second > 1){
                res = true;
                break;
            }
        }
        return res;
    }
};
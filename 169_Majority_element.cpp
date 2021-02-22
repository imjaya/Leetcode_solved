class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> v2c;
        for (auto elem : nums)
            ++v2c[elem];
        for (auto vc : v2c)
            if (2 * vc.second > nums.size())
                return vc.first;
        return 0;
    }
};
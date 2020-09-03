class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int i, n=nums.size(), pro=1;
        vector<int>arr(n, 1);
        pro=nums[0];
        for(i=1; i<n; i++){
            arr[i]=pro;
            pro*=nums[i];
        }
        pro=nums[n-1];
        for(i=n-2; i>=0; i--){
            arr[i]*=pro;
            pro*=nums[i];
        }
        return arr;
    }
};
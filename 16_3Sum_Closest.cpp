class Solution {
public:
    
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        if(nums.size() == 3) return (nums[0] + nums[1] + nums[2]);
        int i=0,j = 1;
        int closest_sum = 0;
        int n = nums.size();
        int k = n-1;
        int sum = 0;
        closest_sum = nums[i] + nums[j] + nums[k];
        for(i = 0 ; i < n-2 ; i++){
            j = i+1;
            k = n-1;
            while(j < k){
                sum = nums[i] + nums[j] + nums[k];
                if(abs(target-sum) < abs(target-closest_sum))
                    closest_sum = sum;
                if(sum < target)
                    j++;
                else
                    k--;
            }
        }
        return closest_sum;
    }

};
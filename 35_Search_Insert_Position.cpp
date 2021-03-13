class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (target>nums[nums.size()-1])
            return nums.size();
        int mid;
        int low=0;
        int high=nums.size()-1;
            
            while(low<=high){
            mid=low+(high-low)/2;
            if(nums[mid]==target){
                return mid;
            }
            if(nums[mid]<target){
                low=mid+1;
            }
            else{
                high=mid-1;
            }
        }
        
        if(nums[mid]>target){
            return mid;
        }
        return mid+1;
    }
};
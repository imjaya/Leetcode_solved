class Solution {
public:
   vector<int> twoSum(vector<int>& numbers, int target) {
       int left = 0, right = numbers.size()-1; 
       vector<int> ret; 
       while (left < right){
           int mid = left + (right-left)/2; 
           int sum = numbers[left] + numbers[right]; 
           if (sum == target){
               ret.push_back(left+1); 
               ret.push_back(right+1); 
               break; 
           }
           else if (sum < target){
               left = (numbers[mid] + numbers[right] < target)?mid:left+1;
           }else{
               right = (numbers[mid] + numbers[left] > target)?mid:right-1;
           }
          
       }
       return ret; 
   }
};
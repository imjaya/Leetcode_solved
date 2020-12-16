class Solution {
public:
    void backtrack(vector<int> &nums,int size,vector<bool> &visited,vector<int> &curr,int index,vector<vector<int> >&ans){
        curr.push_back(nums[index]);
        visited[index]=true;
        if(curr.size()==size){
            ans.push_back(curr);
            curr.pop_back();
            visited[index]=false;
            return;
        }
        for(int i=0;i<size;i++){
            if(visited[i]==false){
                backtrack(nums,size,visited,curr,i,ans);
            }
        }
        visited[index]=false;
        curr.pop_back();
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int> > ans;
        int size=nums.size();
        vector<bool> visited(size,false);
        vector<int> curr;
        for(int i=0;i<size;i++){
            backtrack(nums,size,visited,curr,i,ans);
        }
        return ans;
    }
};
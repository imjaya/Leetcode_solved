/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void solve(TreeNode* root, int targetSum, int currSum, vector<int> vec, vector<vector<int>> &ans){    
        if(root==NULL) return;
        currSum+=root->val;
        vec.push_back(root->val);
        if(currSum==targetSum){
            if(!root->left and !root->right)
            ans.push_back(vec);
        }        
        solve(root->left,targetSum,currSum,vec,ans);
        solve(root->right,targetSum,currSum,vec,ans);   
    }
    
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> ans;
        if(root==NULL) return ans;
        vector<int> vec;
        int currSum=0;
        solve(root,targetSum,currSum,vec,ans);
        return ans;
    }
};
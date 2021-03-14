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
    bool hasPathSum(TreeNode* root, int targetSum) {
        
        // cout<<targetSum<<endl;
        if(!root) return false;
        targetSum-=root->val;
        if(root->right==NULL && root->left==NULL) return targetSum==0;
        
        return (hasPathSum(root->right,targetSum)||hasPathSum(root->left,targetSum));
        
    }
};
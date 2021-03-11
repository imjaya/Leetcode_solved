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
    bool isValidBSTUtil(TreeNode* node, long min, long max) {
        if (node==NULL) return true;
        
        if (node->val <= min || node->val >= max)
            return false;
        
        return isValidBSTUtil(node->left, min, node->val) && isValidBSTUtil(node->right, node->val, max);
    }
    
    bool isValidBST(TreeNode* root) {
        // The tree is empty, and hence, return true
        if(root == NULL) return true;
        // Check if the tree is BST with the utility function
        // As the contraint says -2^31 <= Node.val <= 2^31 - 1, let's select long data type
        return (isValidBSTUtil(root, LONG_MIN, LONG_MAX));
    }
};
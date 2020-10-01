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
    vector<vector<int>>vec;
    void traverse(TreeNode *root, int level) {
        if (root == NULL) return;
        if(level==vec.size())
            vec.push_back(vector<int> ());
        if(!(level&1)) {
            vec[level].push_back(root->val);
        } else {
            vec[level].insert(vec[level].begin(), root->val);
        }
        traverse(root->left, level+1);
        traverse(root->right, level+1);
    }
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        traverse(root,0);
        return vec;
    }
};
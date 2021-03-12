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
    size_t search(const int* array, size_t n, const int& needle) {
        for (size_t i = 0; i < n; i++) {
            if (array[i] == needle) {
                return i;
            }
        }
        return n;
    }
    
    TreeNode* buildTreeFast(const int* preorder, size_t preorder_n, const int* inorder, size_t inorder_n) {
        if (preorder_n == 0 || inorder_n == 0) {
            return NULL;
        }
        
        // this could be `TreeNode* root = new TreeNode(*preorder);`, but I choose to 
        // always treat pointers like arrays just for consistency
        TreeNode* root = new TreeNode(preorder[0]);
        
        auto midpoint = search(inorder, inorder_n, root->val);
            
        root->left = buildTreeFast(preorder + 1, preorder_n - 1, inorder, midpoint);
        root->right = buildTreeFast(preorder + 1 + midpoint, preorder_n - 1 - midpoint, inorder + 1 + midpoint, inorder_n - 1 - midpoint);
        
        return root;
    }
    
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        // because c++ std doesn't provide a way for us to pass slices or references to 
        // parts of a vector, let's just use the underlying array with `std::vector.data()`
        return buildTreeFast(preorder.data(), preorder.size(), inorder.data(), inorder.size());
    }
};
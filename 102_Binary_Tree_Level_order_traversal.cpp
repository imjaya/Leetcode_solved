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
   /** Basic BFS for level order traversal of binary tree */
    vector<vector<int>> levelOrder(TreeNode* root) {
//Base case:

        if(!root) return{};
//Enqeue root to begin BFS

        vector<vector<int>> out; 
        queue<TreeNode*> nodes;
        nodes.push(root);
//Take advantage of knowning size of level to reserve space in array

       TreeNode* front;
       vector<int> level;
       
       while(!nodes.empty()){
           int size = nodes.size(); 
           level.reserve(size);
           
           // Loop through each of the elements in this level
           for(int i=0;i<size;i++){
               front = nodes.front();
               nodes.pop();
               level.push_back(front->val);
               if(front->left) nodes.push(front->left);
               if(front->right) nodes.push(front->right);
           }
           out.push_back(level);
           level.clear();
       }
       return out;
   }
};
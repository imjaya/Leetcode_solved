class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
	/*base cases*/
        if(t1==NULL)
            return t2;
        if(t2==NULL)
            return t1;
			
			/*add up the node values of both the tree into t1 's node*/
        t1->val=t1->val+t2->val;
		
		/*call the recursive function for the left subtrees of both the trees*/
        t1->left=mergeTrees(t1->left,t2->left);
		
		/*call the recursive function for the right subtrees of  both the trees*/
        t1->right=mergeTrees(t1->right,t2->right);
		
		/*finally return the merged tree*/
        return t1;
    }
};
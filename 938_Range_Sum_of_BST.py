# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.ans=0
        def helper(node):
            if node:
                if(node.val>=low and node.val<=high):
                    self.ans+=node.val
                if(low<node.val):
                    helper(node.left)
                if(node.val<high):
                    helper(node.right)
                    
        helper(root)
        return (self.ans)
        
        
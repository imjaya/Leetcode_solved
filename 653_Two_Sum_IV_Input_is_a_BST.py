# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        hasher={}
        def helper(node):
            if not node:
                return False
            if(k-node.val in hasher):
                return True
            hasher[node.val]=True
            
            return helper(node.right) or helper(node.left)
        return helper(root)
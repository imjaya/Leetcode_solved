# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        def helper(node):
            if(node):
                result.append(node.val)
                if(node.left):
                    helper(node.left)
                if(node.right):
                    helper(node.right)
                    
        helper(root)
        return result
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, remainingSum, pathNodes, pathsList):
        
        if not node:
            return 
        
        pathNodes.append(node.val)
        
    
        if remainingSum == node.val and not node.left and not node.right:
            pathsList.append(list(pathNodes))
        else:    
            self.helper(node.left, remainingSum - node.val, pathNodes, pathsList)
            self.helper(node.right, remainingSum - node.val, pathNodes, pathsList)
            

        pathNodes.pop()    
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        pathsList = []
        self.helper(root, sum, [], pathsList)
        return pathsList
        
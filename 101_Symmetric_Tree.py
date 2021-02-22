class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def _symmetric(n1, n2):        
            if not n1 and not n2:
                return True
            if (not n1 and n2) or (not n2 and n1):
                return False
            return n1.val == n2.val and _symmetric(n1.left, n2.right) and _symmetric(n1.right, n2.left)
           
        return _symmetric(root, root)
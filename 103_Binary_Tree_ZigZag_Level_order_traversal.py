# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        q = [root]
        toggle = False
        output = []
        while q:
            out_arr = [x.val for x in q]
            if toggle: out_arr.reverse()
            output.append(out_arr)
            prev_q, q = q, []
            for i in range(0, len(prev_q)):
                elem = prev_q[i]
                if elem.left: q.append(elem.left)
                if elem.right: q.append(elem.right)
            toggle = not toggle
        return output
        
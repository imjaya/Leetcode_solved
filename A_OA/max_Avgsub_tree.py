def subtreeMaxAvg(root: TreeNode) -> TreeNode:
    
    maxavg=[0]
    return_root=0
    def dfs(node: TreeNode):
        if not node: 
            return 0
        total = node.val
        for ch in node.children:
            _,t = dfs(ch)
            total+=t
        avg = total/(1 + len(node.children))
        if(avg>maxavg[0]):
            return_root=node
            maxavg[0] = max(maxavg[0], avg)
        return return_root,avg
    
    return dfs(root)
                    
n = TreeNode(10)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n.children.extend([n1,n2,n3])
print(subtreeMaxAvg(n)[0].val)
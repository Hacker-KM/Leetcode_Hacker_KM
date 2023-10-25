# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node,rank):
            if node:
                if rank == depth-1:
                    newnode = TreeNode(val)
                    newnode.left = node.left
                    node.left = newnode
                    newnode = TreeNode(val)
                    newnode.right = node.right
                    node.right = newnode
                else:
                    dfs(node.left,rank+1)
                    dfs(node.right,rank+1)
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        dfs(root,1)
        return root
        

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node,minv,maxv):
            if node is None:
                return 0
            res = max(abs(node.val-minv), abs(node.val-maxv))
            maxv = max(node.val,maxv)
            minv = min(node.val,minv)
            return max(res,dfs(node.left,minv,maxv),dfs(node.right,minv,maxv))
        return dfs(root,root.val,root.val)
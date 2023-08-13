# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l = {}
        def dfs(node,rank):
            if not node:
                return
            if rank in l:
                l[rank].append(node.val)
            else:
                l[rank] = [node.val]
            dfs(node.left,rank+1)
            dfs(node.right,rank+1)
        dfs(root,0)
        ans = []
        for value in l.values():
            ans.append(value)
        return ans
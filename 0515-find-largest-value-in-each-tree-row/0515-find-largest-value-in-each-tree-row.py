# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ranks = {}
        def dfs(node,rank):
            if node:
                if rank in ranks:
                    ranks[rank].append(node.val)
                else:
                    ranks[rank] = [node.val]
            if node.left:
                dfs(node.left,rank+1)
            if node.right:
                dfs(node.right,rank+1)
        dfs(root,0)
        ans = [max(i) for i in list(ranks.values())]
        return ans
            
        
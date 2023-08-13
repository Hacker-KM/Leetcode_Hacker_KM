# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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
        ans = []
        dfs(root,0)
        for values in l.values():
            ans.append(sum(values)/len(values))
        return ans



        
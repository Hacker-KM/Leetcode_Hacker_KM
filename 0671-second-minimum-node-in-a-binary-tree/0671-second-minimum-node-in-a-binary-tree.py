# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        l=[]
        def dfs(node):
            if node is None:
                return 
            l.append(node.val)

            dfs(node.left)
            dfs(node.right)
        dfs(root)
        l = list(set(l))
        l.sort()
        return l[1] if len(l)>=2 else -1
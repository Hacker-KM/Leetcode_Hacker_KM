# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, l):
            if not node:
                return l
            if node.left is None and node.right is None:
                l.append(node.val)
            l = dfs(node.left, l)
            l = dfs(node.right, l)
            return l

        list1 = dfs(root1, [])
        list2 = dfs(root2, [])
        
        return list1 == list2

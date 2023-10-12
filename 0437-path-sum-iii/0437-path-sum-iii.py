# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, add):
            nonlocal ans
            if not node:
                return
            if add + node.val == targetSum:
                ans += 1
            if node.left:
                dfs(node.left, add + node.val)
            if node.right:
                dfs(node.right, add + node.val)

        ans = 0
        if root:
            stack = [root]

            while stack:
                node = stack.pop()
                dfs(node, 0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return ans

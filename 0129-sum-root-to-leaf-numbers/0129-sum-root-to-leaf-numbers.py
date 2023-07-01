# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l = []
        def helper(node, s):
            if node is None:
                return
            s += str(node.val)
            if node.left is None and node.right is None:
                l.append(int(s))
            helper(node.left, s)
            helper(node.right, s)

        helper(root, "")
        return sum(l)


        
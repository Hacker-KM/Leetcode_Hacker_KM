# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        l = []
        def Preorder(node):
            if node is None:
                return
            l.append(node.val)
            Preorder(node.left)
            Preorder(node.right)
        Preorder(root)
        return len(l)
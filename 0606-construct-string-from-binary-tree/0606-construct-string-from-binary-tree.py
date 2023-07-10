# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ''
        s = []
        
        def helper(root):
            if root is None:
                return
            
            s.append(str(root.val))
            
            if root.left or root.right:
                s.append('(')
                helper(root.left)
                s.append(')')
            
            if root.right:
                s.append('(')
                helper(root.right)
                s.append(')')
        
        helper(root)
        return ''.join(s)


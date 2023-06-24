# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node,miin,maax):
            if node is None:
                return True
            
            if node.val<=miin or node.val>=maax:
                return False
            return helper(node.left,miin,node.val) and helper(node.right,node.val,maax)
        return helper(root,float(-inf),float(inf))
            
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node1,node2,depth):
            if node1 is None and node2 is None:
                return None
            if depth%2!=0:
                node1.val,node2.val = node2.val,node1.val
            helper(node1.left,node2.right,depth+1)
            helper(node1.right,node2.left,depth+1)
        helper(root.left,root.right,1)
        return root

        
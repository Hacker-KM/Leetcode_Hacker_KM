# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        arr = []
        def inorder(root):
            
            if not root:
                return []
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        l = []
        for i in arr:
            if i >=low and i<=high:
                l.append(i)
        return sum(l)
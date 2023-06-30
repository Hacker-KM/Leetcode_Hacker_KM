# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        l = []
        def inorder(node):
            if node is None:
                return 
            inorder(node.left)
            l.append(node)
            inorder(node.right)
        inorder(root)
        a = l[0] 
        for i in range(1,len(l)):
            if l[i].val < l[i-1].val:
                a = l[i-1]
                break
        b = l[-1]  
        for i in range(len(l)-2,-1,-1):
            if l[i].val > l[i+1].val:
                b = l[i+1]
                break
        a.val,b.val = b.val,a.val       


        
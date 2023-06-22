# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:   
        if not root:
            return None
        if root.val > key:			
            root.left = self.deleteNode( root.left, key )
        elif root.val < key:
            root.right = self.deleteNode( root.right, key )
        else:
            if root.left is None and root.right is not None:
                root = root.right 
            elif root.left is not None and root.right is None:
                root = root.left
            elif root.left is None and root.right is None:
                root = None
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.val = cur.val
                root.right = self.deleteNode( root.right, cur.val )               
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = [(root,0,None)]
        imp = []

        if root.val==x or root.val==y:
            imp.append([None,0,root.val])

        while queue:
            node,depth,parent = queue.pop()

            if node.left:
                if node.left.val==x or node.left.val==y:
                    imp.append([node.val,depth+1,node.left.val])
                queue.append((node.left,depth+1,node))

            if node.right:
                if node.right.val==x or node.right.val==y:
                    imp.append([node.val,depth+1,node.right.val])
                queue.append((node.right,depth+1,node))
                
            if len(imp)==2:
                break
 
        if imp[0][1]==imp[1][1] and imp[0][0]!=imp[1][0]:
            return True
        return False

        
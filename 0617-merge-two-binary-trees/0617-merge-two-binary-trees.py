# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        q = deque()
        q.append([root1,root2])
        while q:
            node1,node2 = q.popleft()
            node1.val +=node2.val
            if node1.left is None and node2.left is not None:
                node1.left = node2.left 
            elif node1.left is not None and node2.left is not None:
                q.append([node1.left,node2.left])
            if node1.right is None and node2.right is not None:
                node1.right = node2.right
            elif node1.right is not None and node2.right is not None:
                q.append([node1.right,node2.right])
        return root1
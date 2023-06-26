# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root,0))
        max_depth = 0
        ans =0 
        while q:
            node,depth = q.popleft()
            if depth>max_depth:
                ans = 0
                max_depth = depth
            if depth ==max_depth:
                ans+=node.val
            if node.left:
                q.append((node.left,depth+1))
            if node.right:
                q.append((node.right,depth+1))
        return ans


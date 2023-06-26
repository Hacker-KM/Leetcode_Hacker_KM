# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        if root is None:
            return 0
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            if curr.left and curr.left.left and curr.val%2==0:
                ans+=curr.left.left.val
            if curr.left and curr.left.right and curr.val%2==0:
                ans+=curr.left.right.val
            if curr.right and curr.right.left and curr.val%2==0:
                ans+=curr.right.left.val
            if curr.right and curr.right.right and curr.val%2==0:
                ans+=curr.right.right.val
        return ans
        
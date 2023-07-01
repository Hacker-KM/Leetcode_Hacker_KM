# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        res = []
        def helper(node):
            if node is None:
                return 
            res.append(node.val)
            if node.left is None and node.right is None and sum(res)==targetSum:
                ans.append(list(res))
            else:
                helper(node.left)
                helper(node.right)
            res.pop()
        helper(root)
        return ans
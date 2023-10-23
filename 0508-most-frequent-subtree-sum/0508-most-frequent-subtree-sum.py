# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node):
            if node:
                s = node.val + dfs(node.left) + dfs(node.right)
                ans.append(s)
                return s
            else: return 0
        
        dfs(root)
        l_count = Counter(ans)
    
        freq = list(l_count.values())
        if max(freq)==1:
            return ans
        else:
            p=[]
            for v,fre in l_count.items():
                if fre==max(freq):
                    p.append(v)
            return p
                    

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ranks= {}
        def dfs(node,rank):
            if node:
                if rank in ranks:
                    ranks[rank].append(node.val)
                else:
                    ranks[rank] = [node.val]
            if node.left:
                dfs(node.left,rank+1)
            if node.right:
                dfs(node.right,rank+1)
        dfs(root,0)
        l = list(ranks.values())
        return l[-1][0]
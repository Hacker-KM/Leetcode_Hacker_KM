
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                    stack.append(node.left)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
                    stack.append(node.right)

        def dfs(node, dis, visited, maxDis):
            visited.add(node)
            maxDis[0] = max(maxDis[0], dis)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour, dis + 1, visited, maxDis)

        maxDis = [0]
        dfs(start, 0, set(), maxDis)
        return maxDis[0]


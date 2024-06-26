class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        visited = [False]*len(isConnected)
        def dfs(node):
            visited[node] = True
            for i in range(len(isConnected[node])):
                if isConnected[node][i]==1 and not visited[i]:
                    dfs(i)

        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                ans+=1
        return ans

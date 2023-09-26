class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = [[] for i in range((len(roads)+1))]
        for node1,node2 in roads:
            graph[node1].append(node2)
            graph[node2].append(node1)
        self.ans = 0
        def dfs(node,parent):
            passenger = 0
            for child in graph[node]:
                if child!=parent:
                    p = dfs(child,node)
                    passenger+=p
                    self.ans += int(ceil(p/seats))
            return passenger + 1
        dfs(0,None)
        return self.ans
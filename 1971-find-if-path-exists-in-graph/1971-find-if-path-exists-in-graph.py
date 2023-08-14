class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for i in range(n)]
        for edge in edges:
            u,v = edge
            graph[u].append(v)
            graph[v].append(u)
        visited = [False]*n
        queue = [source]
        while queue:
            node = queue.pop(0)
            if node==destination:
                return True
            if visited[node]:
                continue
            visited[node] = True
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    queue.append(neighbour)
        return False

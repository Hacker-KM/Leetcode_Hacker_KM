class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        components = 0
        graph = [[] for _ in range(n)]
        
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, visited, graph, component):
            visited[node] = True
            component.add(node)
            for adjacent in graph[node]:
                if not visited[adjacent]:
                    dfs(adjacent, visited, graph, component)
        
        for node in range(n):
            if not visited[node]:
                component = set()
                dfs(node, visited, graph, component)
                
                is_complete = True
                for vertex in component:
                    count_neighbors = 0
                    for neighbor in graph[vertex]:
                        if neighbor in component:
                            count_neighbors += 1
                    if count_neighbors != len(component) - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    components += 1
        
        return components

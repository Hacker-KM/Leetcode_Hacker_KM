class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        target = n - 1
        all_paths = []
        queue = [(0, [0])]
        
        while queue:
            node, path = queue.pop(0)  
            
            if node == target:
                all_paths.append(path)  
            else:
                for neighbor in graph[node]:
                    queue.append((neighbor, path + [neighbor]))
        
        return all_paths

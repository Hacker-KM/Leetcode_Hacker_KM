class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adj_list = [[] for i in range(n)]
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        start,end,cost  = edge
        self.adj_list[start].append((end,cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [float('inf')]*self.n
        dist[node1] = 0
        heap = [(0,node1)]
        while heap:
            cost,node = heapq.heappop(heap)
            if cost>dist[node]:
                continue
            if node==node2:
                return dist[node2]
            for neighbour,weight in self.adj_list[node]:
                total_dist = cost+weight
                if total_dist<dist[neighbour]:
                    dist[neighbour] = total_dist
                    heapq.heappush(heap,(total_dist,neighbour))
        return dist[node2] if dist[node2]!=float('inf') else -1
            
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for i in range(n+1)]
        for s,t,w in flights:
            graph[s].append((t,w))
        cost = [float('inf') for i in range(n+1)]
        stops = [float('inf') for i in range(n+1)]
        heap = [(0,src,0)]
        while heap:
            total_cost,node,current_stops = heapq.heappop(heap)
            if node==dst:
                return total_cost
            if current_stops>k:
                continue
            for neighbour, edge_cost in graph[node]:
                new_cost = total_cost + edge_cost
                if new_cost < cost[neighbour] or current_stops + 1 < stops[neighbour]:
                    cost[neighbour] = new_cost
                    stops[neighbour] = current_stops + 1
                    heapq.heappush(heap, (new_cost, neighbour, current_stops + 1))
        return -1

            
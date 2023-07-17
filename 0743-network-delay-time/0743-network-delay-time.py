

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        for s, t, w in times:
            graph[s].append((t, w))
        distance = [float('inf') for _ in range(n+1)]
        distance[k] = 0
        heap = [(0, k)]
        while heap:
            time, node = heapq.heappop(heap)
            if time < distance[node]:
                print(time,distance[node])
                continue
            for neighbour, ntime in graph[node]:
                totalt = ntime + time
                if totalt < distance[neighbour]:
                    distance[neighbour] = totalt
                    heapq.heappush(heap, (totalt, neighbour))
        

        max_d = max(distance[1:])
        return max_d if max_d < float('inf') else -1


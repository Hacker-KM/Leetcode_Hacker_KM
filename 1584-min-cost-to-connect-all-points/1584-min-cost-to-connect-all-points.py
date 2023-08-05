class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calculate_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i+1,n):
                distance = calculate_distance(points[i],points[j])
                edges.append((i,j,distance))
        edges.sort(key=lambda x:x[2])
        parents = list(range(n))
        ranks = [0]*n
        min_cost = 0
        def find(i):
            if parents[i]!=i:
                parents[i] = find(parents[i])
            return parents[i]
        def union(i,j):
            rooti = find(i)
            rootj = find(j)
            if rooti!=rootj:
                if ranks[rooti]<=ranks[rootj]:
                    parents[rooti] = rootj
                    ranks[rootj]+=1
                else:
                    parents[rootj] = rooti
                    ranks[rooti]+=1
        for v,u,distance in edges:
            if find(u)!=find(v):
                min_cost+=distance
                union(u,v)
        return min_cost

        
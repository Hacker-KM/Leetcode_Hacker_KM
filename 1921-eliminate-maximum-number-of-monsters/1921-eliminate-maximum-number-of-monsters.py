class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        time = [0]*n
        for i in range(n):
            time[i] = ceil(dist[i]/speed[i])
        time.sort()
        for i in range(n):
            if time[i]<=i:
                return i
        return n
        
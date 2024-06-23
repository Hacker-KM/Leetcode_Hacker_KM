class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        l = [-a,-b,-c]
        l.sort()
        ans = 0
        while l.count(0)<2 :
            n = heapq.heappop(l)
            m = heapq.heappop(l)
            heapq.heappush(l,n+1)
            heapq.heappush(l,m+1)
            ans+=1
        return ans


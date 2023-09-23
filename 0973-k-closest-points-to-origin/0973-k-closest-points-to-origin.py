class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l = []
        def distance(i,j):
            l.append([i,j,i*i+j*j])
        for i,j in points:
            distance(i,j)
        l.sort(key = lambda x:x[2])
        ans = []
        for i in range(k):
            ans.append(l[i][:2])
        return ans
        
        
        
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        p = sorted(points)
        l = []
        arr = [x for x,y in p]
        for i in range(1,len(arr)):
            l.append(arr[i]-arr[i-1])
        return max(l)
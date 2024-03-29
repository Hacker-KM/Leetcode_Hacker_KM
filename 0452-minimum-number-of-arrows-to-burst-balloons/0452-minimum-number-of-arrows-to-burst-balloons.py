class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        target = points[0][1]
        ans = 1
        for start,end in points:
            if start <= target <= end:
                continue
            else:
                ans+=1
                target = end
        return ans
                
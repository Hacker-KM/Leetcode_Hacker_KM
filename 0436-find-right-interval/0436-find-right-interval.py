class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if len(intervals)<2 and intervals[0][0]!=intervals[0][1]:
            return [-1]
        elif len(intervals)<2 and intervals[0][0]==intervals[0][1]:
            return [0]
        start = [s for s,e in intervals]
        end = [e for s,e in intervals]
        start_sorted = sorted(start)
        end_sorted = sorted(end)
        ans = []
        for i in end:
            index = bisect_left(start_sorted, i)
            if index>len(start)-1:
                ans.append(-1)
            else:
                ans.append(start.index(start_sorted[index]))
        return ans
        
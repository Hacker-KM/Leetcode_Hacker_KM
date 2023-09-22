# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         for i in range(len(intervals)-1):
#             [start,end] = intervals[i]
#             if end<newInterval[0]:
#                 continue
#             if start<=newInterval[0] and intervals[i+1][0]>=newInterval[0]:
#                 # print(intervals[i+1][0])
#                 intervals[i][0] = start
#                 intervals[i][1] = newInterval[1]
#                 # print(intervals[i])
#                 if intervals[i+1][1]<intervals[i][1]:
#                     intervals.remove(intervals[i+1])
#                 # print(intervals[i+1])
#                 if intervals[i+1][0]==intervals[i][1]:
#                     intervals[i][1] = intervals[i+1][1]
#                     break
#         # print(intervals)
#         for i in range(len(intervals)-1):
#             if intervals[i][1]>=intervals[i+1][0] and intervals[i+1][1]>=intervals[i][1]:
#                 intervals[i][1] = intervals[i+1][1]
#                 intervals.remove(intervals[i+1])
#                 break
#         return intervals


####Copied from solutionnnnnnn#############



class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = []
        for i in intervals:
            if i[1] < newInterval[0]:
                l.append(i)
            elif i[0] > newInterval[1]:
                l.append(newInterval)
                newInterval = i
            elif i[1] >= newInterval[0] or i[0] <= newInterval[1]:
                newInterval[0] = min(i[0],newInterval[0])
                newInterval[1] = max(newInterval[1],i[1])
        l.append(newInterval)
        return l




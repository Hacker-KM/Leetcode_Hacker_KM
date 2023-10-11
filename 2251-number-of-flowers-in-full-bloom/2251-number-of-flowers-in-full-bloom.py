# class Solution:
#     def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # ans = []
        # for i in people:
        #     c = 0
        #     for j in flowers:
        #         if j[1]>=i>=j[0]:
        #             c+=1
        #     ans.append(c)
        # return ans

        # copied Solution
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = sorted([s for s, e in flowers])
        end = sorted([e for s, e in flowers])
        return [bisect_right(start, t) - bisect_left(end, t) for t in people]
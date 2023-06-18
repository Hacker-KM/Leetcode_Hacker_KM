class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        ans= []
        for i in set(nums):
            l.append([nums.count(i),i])
        l.sort()
        l.reverse()
        for i in range(k):
            ans.append(l[i][1])
        return ans
        

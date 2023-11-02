class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        l = []
        for i in range(len(nums)+1):
            for j in range(i+1,len(nums)+1):
                l.append(len(set(nums[i:j]))**2)
        return sum(l)

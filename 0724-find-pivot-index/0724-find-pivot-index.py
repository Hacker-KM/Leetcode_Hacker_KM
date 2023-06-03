class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        for k in range(l):
            if sum(nums[:k])==sum(nums[k+1:]):
                return k
        return -1
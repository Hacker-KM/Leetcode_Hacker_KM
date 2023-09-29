class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        t = sorted(nums)
        return t==nums or t[::-1]==nums
        
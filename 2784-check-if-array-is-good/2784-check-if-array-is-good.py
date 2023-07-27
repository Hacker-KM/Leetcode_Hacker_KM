class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)  
        b = list(range(1, n)) + [n, n]  
        if sorted(nums) == b:
            return True
        else:
            return False
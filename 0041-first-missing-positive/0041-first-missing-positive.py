class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        p = set(nums)
        i =1
        while i in p:
            i+=1
        return i
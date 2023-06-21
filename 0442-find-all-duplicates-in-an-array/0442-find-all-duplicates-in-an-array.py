class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l = []
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                l.append(nums[i])
        return l
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        l = []
        for i in range(len(nums)-1,0,-1):
            l.append(nums[i]-nums[i-1])
        return max(l) if len(nums)>1 else 0
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        for i in range(len(nums)):
            temp = nums[i+1:]+nums[:i]
            for j in temp:
                if j>nums[i]:
                    ans[i] = j
                    break
        return ans
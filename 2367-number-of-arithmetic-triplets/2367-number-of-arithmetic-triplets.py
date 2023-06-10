class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                p = diff+nums[j]
                if nums[j] - nums[i] == diff and (p in nums) and nums.index(p)>j:
                    ans+=1
        return ans


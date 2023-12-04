class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums = [num for num in nums if num != 0]
        def mul(arr):
            ans = 1
            for i in arr:
                ans*=i
            if 1 in nums or nums.count(-1)==2:
                return ans
            else:
                return ans if ans!=1 else 0
        countNeg = 0
        MaxNeg = -float('inf')
        for i in nums:
            if i<0:
                countNeg+=1
                MaxNeg = max(i,MaxNeg)
        if countNeg%2==0:
            return mul(nums)
        else:
            i = nums.index(MaxNeg)
            nums.remove(nums[i])
            return mul(nums)
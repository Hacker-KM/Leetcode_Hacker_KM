class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        goal = sum(nums)-x
        if goal == 0:
            return len(nums)
        if goal<0:
            return -1
        left = 0
        temp_sum = 0
        ans = 0
        for right in range(len(nums)):
            temp_sum+=nums[right]
            while left<=right and temp_sum>goal:
                temp_sum-=nums[left]
                left+=1
            if temp_sum==goal:
                ans = max(ans,right-left+1)
        return -1 if ans== 0 else len(nums)-ans
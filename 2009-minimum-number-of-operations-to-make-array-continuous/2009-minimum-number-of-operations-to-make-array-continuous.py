class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        ans = float('inf')

        for i in range(len(nums)):
            s = nums[i]
            e = s + n - 1
            idx = self.find_index(nums, e)

            ans = min(ans, n - (idx - i + 1))
        
        return ans

    def find_index(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        lis_lengths = [1] * n

        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j] and lis_lengths[i] < lis_lengths[j] + 1:
                    lis_lengths[i] = lis_lengths[j] + 1

        return max(lis_lengths)
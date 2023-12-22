from typing import List

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        ans = 0

        def check(subarray):
            count = 0
            for num in subarray:
                if num % p == 0:
                    count += 1
            return count <= k

        distinct_subarrays = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                subarray = nums[i:j]
                if check(subarray):
                    distinct_subarrays.add(tuple(subarray))

        return len(distinct_subarrays)

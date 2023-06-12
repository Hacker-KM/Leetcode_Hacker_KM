class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        diff = float('inf')
        n = len(nums)
        for i in range(n-2):
            j = i+1
            k = n-1
            while j<k:
                sums = nums[i] + nums[j] + nums[k]
                if sums == target:
                    return sums
                if abs(sums-target) <= diff:
                    diff = abs(sums-target)
                    ans = sums
                if sums < target:
                    j += 1
                else:
                    k -= 1
        
        return ans
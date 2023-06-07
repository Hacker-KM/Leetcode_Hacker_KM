class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return nums[0]==1
        div = gcd(nums[0], nums[1])

        if len(nums) == 2:
            return div==1

        for i in range(1, len(nums) - 1):
            div = gcd(div, nums[i + 1])
        return div == 1
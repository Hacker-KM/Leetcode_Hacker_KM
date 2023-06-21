class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        c= 0
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                if nums[j]-nums[j-1] == nums[j+1]-nums[j]:
                    c += 1
                    j += 1
                else:
                    break
        return c

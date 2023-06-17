class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans= []
        for i in set(nums):
            l = nums.count(i)
            if l>len(nums)/3:
                ans.append(i)
        return list(set(ans))
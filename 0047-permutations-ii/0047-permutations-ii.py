class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l = list(itertools.permutations(nums))
        ans = []
        for i in l:
            if i not in ans:
                ans.append(i)
        return ans
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        comb = []
        ans= 0
        for i in range(len(nums)+1):
            comb += [list(j) for j in combinations(nums, i)]
        for i in comb:
            if i!=[]:
                ans+=reduce(ixor, i)
        return ans
        
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1,2,3,4,5,6,7,8,9]
        subset = combinations(nums,k)
        ans = []
        for i in subset:
            if sum(i)==n:
                ans.append(i)
        return ans
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        def solve(n,m):
            if n==m:
                return nums[n]
            elif (n,m) in dp:
                return dp[(n,m)]
            else:
                c = max(nums[n]-solve(n+1,m),nums[m]-solve(n,m-1))
                dp[(n,m)] = c
            return c
        return solve(0,len(nums)-1)>=0
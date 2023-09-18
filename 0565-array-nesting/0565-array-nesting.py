class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans = 0
        visited = [False]*len(nums)
        def dfs(index):
            if not visited[index]:
                visited[index] = True
                return 1+dfs(nums[index])
            else:
                return 0
            
        for i in range(len(nums)):
            if not visited[i]:
                ans = max(ans,dfs(i))
        
        return ans

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = [""]
        n = len(nums)
        while n>0:
            temp = []
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                else:
                    temp.append(nums[i])
                    visited.append(nums[i])
                    nums[i]=""
            ans.append(temp)
            n-=len(temp)
            visited = [""]
        return ans


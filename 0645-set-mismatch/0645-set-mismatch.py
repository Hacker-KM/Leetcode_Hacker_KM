class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        temp=1
        for i in nums:
            if nums.count(i)==2:
                ans.append(i)
                break
        if (ans[0]-1)>0 and (ans[0]-1) not in nums:
            ans.append(ans[0]-1)
        elif (ans[0]+1) not in nums:
            ans.append(ans[0]+1)
        while len(ans)!=2:
            if temp not in nums:
                ans.append(temp)
            else:
                temp+=1

        return ans 
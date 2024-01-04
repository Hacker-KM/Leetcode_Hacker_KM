class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = Counter(nums)
        ans = 0
        for i in n.values():
            n = i%3
            if i==1:
                return -1
            elif i==2 or i==3:
                ans+=1
            elif n!=0:
                ans+=i//3 + 1
            elif n==0:
                ans+=i//3
        return ans
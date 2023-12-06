class Solution:
    def totalMoney(self, n: int) -> int:
        temp = 0
        i = 1
        j = 1
        ans = 0
        while temp<n:
            if temp%7!=0 or temp==0:
                ans+=i
                i+=1
                temp+=1
            else:
                i = j+1
                j=i
                ans+=i
                temp+=1
                i+=1
        return ans

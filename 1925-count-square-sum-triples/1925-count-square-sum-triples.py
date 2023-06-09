class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                k = math.sqrt(i*i + j*j)
                if int(k)==k and k<=n:
                    ans+=2
        return ans
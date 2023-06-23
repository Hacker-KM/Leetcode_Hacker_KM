class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        r=0
        for i in range(1,k+1):
            r= (r*10 +1)
            if r%k==0:
                return i
        return -1
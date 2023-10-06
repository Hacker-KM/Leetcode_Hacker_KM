class Solution:
    def lastRemaining(self, n: int) -> int:

        # Mine TLE solution

        # if n==0:
        #     return 0
        # if n==1:
        #     return 1
        # m = n//2 +1
        # l = [i for i in range(m,n+1)]
        # while len(l)>1:
        #     l = l[1::2]
        #     l.reverse()
        # return l[0]

        # RECURSION

        return 1 if n==1 else 2*(n//2 +1-self.lastRemaining(n//2))
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        l = [1]
        for i in range(2,n//2+1):
            if n%i==0:
                l.append(i)
        l.append(n)
        return l[k-1] if len(l)>=k else -1
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num = ''
        for i in range(1,n+1):
            num+=str(i)
        l = [list(perm) for perm in itertools.permutations(num)]
        ans = ''.join(l[k-1])
        return ans
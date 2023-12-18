class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        l = set()
        for i in range(len(s)-k+1):
            l.add(s[i:i+k])
        return 2**k==len(l)

        
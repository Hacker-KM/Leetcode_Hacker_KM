class Solution:
    def maxScore(self, s: str) -> int:
        ans = -float('inf')
        for i in range(1,len(s)):
            s1 = s[:i].count("0")
            s2 = s[i:].count("1")
            ans = max(ans,s1+s2)
        return ans
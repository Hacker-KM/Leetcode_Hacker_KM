class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        l = combinations(words,2)
        for s1,s2 in l:
            if not set(s1)&set(s2):
                ans = max(ans,len(s1)*len(s2))
        return ans
        
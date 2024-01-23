class Solution:
    def maxLength(self, arr: List[str]) -> int:
        l = []
        for r in range(len(arr) + 1):
            l.extend(list(combinations(arr, r)))
        ans = 0
        for i in l:
            temp = "".join(i)
            if len(set(list(temp)))==len(temp):
                ans = max(ans,len(temp))
        return ans
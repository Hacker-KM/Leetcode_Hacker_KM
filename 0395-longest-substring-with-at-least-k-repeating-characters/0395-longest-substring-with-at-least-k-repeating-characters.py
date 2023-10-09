class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0

        char_count = Counter(s)
        i = 0

        while i < len(s) and char_count[s[i]] >= k:
            i += 1

        if i == len(s):
            return len(s)  

        left = self.longestSubstring(s[:i], k)
        right = self.longestSubstring(s[i + 1:], k)
        return max(left, right)
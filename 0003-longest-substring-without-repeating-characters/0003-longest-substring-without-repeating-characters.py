class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        visited = set()
        max_length = 0
        i = 0
        j = 0

        while j < len(s):
            if s[j] not in visited:
                visited.add(s[j])
                j += 1
                max_length = max(max_length, j - i)
            else:
                visited.remove(s[i])
                i += 1

        return max_length

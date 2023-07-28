class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        ans = ""
        j = 0
        while j < len(strs[0]):
            current_char = strs[0][j]
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != current_char:
                    return ans
            ans += current_char
            j += 1

        return ans

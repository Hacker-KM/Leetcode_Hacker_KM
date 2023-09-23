class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        ans = 0
        track = [1] * len(words)
        
        for i in range(1, len(words)):
            for j in range(i):
                if self.helper(words[j], words[i]):
                    track[i] = max(track[i], track[j] + 1)
        
        return max(track)

    def helper(self, word1: str, word2: str) -> bool:
        if len(word1) + 1 != len(word2):
            return False
        
        i, j = 0, 0
        diff_count = 0

        while i < len(word1) and j < len(word2):
            if word1[i] == word2[j]:
                i += 1
                j += 1
            else:
                diff_count += 1
                j += 1

            if diff_count > 1:
                return False

        return True

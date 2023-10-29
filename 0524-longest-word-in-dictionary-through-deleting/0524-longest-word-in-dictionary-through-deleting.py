class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: len(x), reverse=True)
        l = []
        length = []
        for word in dictionary:
            j = 0
            for i in range(len(s)):
                if j < len(word) and s[i] == word[j]:
                    j += 1
            if j == len(word):
                l.append(word)
                length.append(len(word))
        l.sort()
        for i in l:
            if len(i)==max(length):
                return i
        return ""  


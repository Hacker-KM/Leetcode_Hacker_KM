class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = s.split()
        l = []
        l1 = []
        for i in pattern:
            l.append(pattern.index(i))
        for i in s:
            l1.append(s.index(i))
        return l==l1
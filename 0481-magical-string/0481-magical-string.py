class Solution:
    def magicalString(self, n: int) -> int:
        s = [1, 2, 2]
        i = 2
        while len(s) < n:
            count = s[i]
            if s[-1] == 2:
                s += [1] * count
            else:
                s += [2] * count
            i += 1
        return s[:n].count(1)

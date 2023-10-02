class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        print(s)
        if not s:
            return 0

        neg = False
        if s[0] == "-":
            neg = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        ans = 0
        digitdic = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}

        for i in s:
            if i not in digitdic:
                break
            ans = ans * 10 + digitdic[i]

        if neg:
            ans = -ans

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        return max(min(ans, INT_MAX), INT_MIN)
        
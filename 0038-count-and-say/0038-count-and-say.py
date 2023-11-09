class Solution:
    def countAndSay(self, n: int) -> str:
        def helper1(s):
            l = []
            c = 1
            for i in range(len(s)):
                if i == len(s) - 1 or s[i] != s[i + 1]:
                    l.append([int(s[i]), c])
                    c = 1
                else:
                    c += 1
            return l

        def helper2(l):
            s = ''
            for i in l:
                s += str(i[1]) + str(i[0])
            return s

        result = "1"
        for _ in range(n - 1):
            pairs = helper1(result)
            result = helper2(pairs)

        return result

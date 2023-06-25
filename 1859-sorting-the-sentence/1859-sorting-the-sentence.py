class Solution:
    def sortSentence(self, s: str) -> str:
        l = s.split()
        r = []
        for i in l:
            r.append(i[::-1])
        r.sort()
        for i in range(len(r)):
            r[i] = r[i][1:len(r[i])][::-1]
        ans = ' '.join(r)
        return ans
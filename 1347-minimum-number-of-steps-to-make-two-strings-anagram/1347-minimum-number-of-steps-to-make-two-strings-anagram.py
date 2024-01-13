class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # c= 0
        # t= list(t)
        # for i in range(len(s)):
        #     if s[i] in t:
        #         t.remove(s[i])
        #     else:
        #         c+=1
        # return c
        return sum((Counter(t)-Counter(s)).values())
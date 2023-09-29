class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
# TLE
        # i = 0
        # s1 = list(s1)
        # s2 = list(s2)
        # while i<len(s1):
        #     j = i+2
        #     while j < len(s1):
        #         if s1[i]!=s2[i] and s1[j]!=s2[j]:
        #             s1[i],s1[j] = s1[j],s1[i]
        #         if s1[i]==s2[i]:
        #             break
        #         j+=2
        #     i+=1
        # return s1==s2

# ONE LINER
        return sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2])==sorted(s2[1::2])
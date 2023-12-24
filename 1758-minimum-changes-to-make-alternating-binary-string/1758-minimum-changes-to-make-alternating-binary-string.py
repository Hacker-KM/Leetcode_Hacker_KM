class Solution:
    def minOperations(self, s: str) -> int:
        start_0 = 0
        n = len(s)
        start = 0
        for i in s:
            if int(i)!=start:
                start_0+=1
            start = not start
        start_1 = n-start_0
        return min(start_1,start_0)
        
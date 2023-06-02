class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        c = 0
        for i in s:
            if i=='L':
                c+=1
            else:
                c-=1
            if c==0:
                result+=1
        return result
            
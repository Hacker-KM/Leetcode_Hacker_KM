class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left,right = 0,int(sqrt(c))+1
        while left<=right:
            summ = left**2+right**2
            if summ==c:
                return True
            elif summ<c:
                left+=1
            else:
                right-=1
        return False
                    
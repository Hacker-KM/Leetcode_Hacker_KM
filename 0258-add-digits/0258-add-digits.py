class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        temp = float('inf')
        while temp != 1:
            summ = 0
            for i in num:
                summ += int(i)
            temp = len(str(summ))
            num = str(summ)
        return int(num)


    

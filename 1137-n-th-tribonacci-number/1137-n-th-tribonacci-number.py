class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        sum=0
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        for i in range(n-2):
            sum = a+b+c
            a = b
            b= c 
            c= sum
        return sum


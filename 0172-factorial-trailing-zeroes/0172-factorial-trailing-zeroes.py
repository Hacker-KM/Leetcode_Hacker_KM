class Solution:
    def trailingZeroes(self, n: int) -> int:
        temp = math.factorial(n)
        c= 0

        while temp%10==0:
            c+=1
            temp//=10

        return c
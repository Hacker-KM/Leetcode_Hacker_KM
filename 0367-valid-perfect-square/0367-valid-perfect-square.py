class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = sqrt(num)
        m = int(n)
        return n==m
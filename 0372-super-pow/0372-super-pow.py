class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        p = 0
        for i in b:
            p = (p * 10 + i)
        return pow(a, p, 1337)

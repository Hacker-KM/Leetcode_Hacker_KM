class Solution:
    def reverseBits(self, n: int) -> int:
        a = str(bin(n)).replace('0b',"")
        p = 32-len(a)
        l = "0"*p
        a = l+a
        return int(a[::-1],2)
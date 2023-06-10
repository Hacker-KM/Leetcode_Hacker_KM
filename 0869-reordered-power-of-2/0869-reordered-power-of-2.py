class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        a = []
        i =0 
        powernum=2**0
        while powernum<1000000000:
            powernum= 2**i
            a.append(sorted(str(powernum)))
            i+=1
        return sorted(str(n)) in a
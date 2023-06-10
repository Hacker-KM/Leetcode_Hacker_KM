class Solution:
    def sumOddLengthSubarrays(self, l: List[int]) -> int:
        comb = [[]]
        ans= sum(l)
        for i in range(len(l) + 1):
            for j in range(i):
                comb.append(l[j: i])
        for i in comb:
            if len(i)%2!=0 and len(i)>1:
                ans= ans+sum(i)
        return ans
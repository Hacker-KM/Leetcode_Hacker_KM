class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c=[]
        for i in range(min(len(A),len(B))):
            lst1 = A[0:i+1]
            lst2 = B[0:i+1]
            lst3 = [value for value in lst1 if value in lst2]
            c.append(len(lst3))
        return c
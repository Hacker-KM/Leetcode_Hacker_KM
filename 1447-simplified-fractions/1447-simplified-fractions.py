class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        l =[]
        p=[]
        for i in range(1,n):
            for j in range(1,n+1):
                if i/j>0 and i/j<1 and i/j not in p:
                    p.append(i/j)
                    l.append(str(i)+"/"+str(j))
        return l
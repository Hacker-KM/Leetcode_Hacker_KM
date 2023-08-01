class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l = []
        for i in range(1,n+1):
            l.append(i)
        l1= list(itertools.combinations(l,k))
        return l1
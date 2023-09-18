class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l = []
        ans = []
        for i in range(len(mat)):
            l.append([sum(mat[i]),i])
        l.sort(key=lambda x:x[0])
        for i in range(0,k):
            ans.append(l[i][1])
        return ans
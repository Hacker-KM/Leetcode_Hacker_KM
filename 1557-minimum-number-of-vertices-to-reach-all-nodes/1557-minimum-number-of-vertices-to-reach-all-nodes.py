class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = []
        s = set()
        for i,j in edges:
            s.add(j)
        for i in range(n):
            if i not in s:
                ans.append(i)
        return ans                
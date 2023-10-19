class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        i, j = 0, 0
        ans = []
        up = True

        while i < n and j < m:
            ans.append(mat[i][j])
            if up:
                if i == 0 and j < m - 1:
                    j += 1
                    up = not up
                elif j == m - 1:
                    i += 1
                    up = not up
                else:
                    i -= 1
                    j += 1
            else:
                if j == 0 and i < n - 1:
                    i += 1
                    up = not up
                elif i == n - 1:
                    j += 1
                    up = not up
                else:
                    i += 1
                    j -= 1

        return ans

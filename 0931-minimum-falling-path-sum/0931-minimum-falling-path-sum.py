class Solution:
    def minFallingPathSum(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows - 2, -1, -1):
            for col in range(cols):
                matrix[row][col] += min(matrix[row + 1][max(0, col - 1):min(cols, col + 2)])

        return min(matrix[0])
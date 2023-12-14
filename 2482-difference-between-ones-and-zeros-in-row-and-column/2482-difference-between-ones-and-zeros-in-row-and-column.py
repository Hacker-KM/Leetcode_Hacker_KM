class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row = []
        col = []
        for i in range(len(grid)):
            row.append(grid[i].count(1))
        for j in range(len(grid[0])):
            temp = [grid[i][j] for i in range(len(grid))]
            col.append(temp.count(1))
        diff = [[0]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff[i][j] = 2*row[i] + 2*col[j] - len(grid) - len(grid[0])

        return diff

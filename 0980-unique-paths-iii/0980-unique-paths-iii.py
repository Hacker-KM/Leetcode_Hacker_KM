from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        empty = 1
        start = None
        ans = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 0:
                    empty += 1

        def is_valid(i, j):
            return 0 <= i < rows and 0 <= j < cols

        def dfs(i, j, count):
            nonlocal ans

            if not is_valid(i, j) or grid[i][j] == -1:
                return

            if grid[i][j] == 2:
                if count == empty:
                    ans += 1
                return

            temp = grid[i][j]
            grid[i][j] = -1


            dfs(i + 1, j, count + 1)
            dfs(i - 1, j, count + 1)
            dfs(i, j + 1, count + 1)
            dfs(i, j - 1, count + 1)

            grid[i][j] = temp

        [i, j] = start
        dfs(i, j, 0)
        return ans

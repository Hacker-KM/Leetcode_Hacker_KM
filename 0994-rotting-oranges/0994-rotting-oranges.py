from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        minutes = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.pop(0)
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    queue.append((i - 1, j))
                if i + 1 < len(grid) and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    queue.append((i + 1, j))
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    queue.append((i, j - 1))
                if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    queue.append((i, j + 1))
            if queue:
                minutes += 1

        for row in grid:
            if 1 in row:
                return -1

        return minutes

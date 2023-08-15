class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        def bfs(row,col):
            queue = [(row,col)]
            area = 0
            while queue:
                r,c = queue.pop(0)
                if r>=0 and r<len(grid) and c>=0 and c<len(grid[0]) and grid[r][c]==1:
                    grid[r][c]=0
                    area+=1
                    if r + 1 <len(grid):
                        queue.append((r + 1, c))
                    if r - 1 >= 0:
                        queue.append((r - 1, c))
                    if c + 1 < len(grid[0]):
                        queue.append((r, c + 1))
                    if c - 1 >= 0:
                        queue.append((r, c - 1))
            return area
        ans= 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    ans = max(ans,bfs(row,col))
        return ans
            
                    

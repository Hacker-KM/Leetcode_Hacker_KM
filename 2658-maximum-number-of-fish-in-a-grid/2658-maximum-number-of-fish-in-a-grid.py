class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r in range(m):
            for c in range(n):
                if grid[r][c]>0:
                    queue = [(r,c)]
                    count = 0
                    while queue:
                        row,col = queue.pop()
                        if grid[row][col]==0:continue
                        count+=grid[row][col]
                        grid[row][col] = 0
                        for m_r,m_c in directions:
                            new_r,new_c = row+m_r,col+m_c
                            if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] !=0:
                                queue.append((new_r, new_c))
                    ans = max(ans,count)
        return ans
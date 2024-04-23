class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n = len(land)
        m = len(land[0])
        def isvalid(i,j):
            return 0<=i<n and 0<=j<m and land[i][j]==1
        cap = [(0,0)]
        def dfs(x,y):
            land[x][y] = -1
            if x+1>=n and y+1>=m:
                cap.append((x,y))
            elif x+1>=n and y+1<m and land[x][y+1]==0:
                cap.append((x,y))
            elif y+1>=m and x+1<n and land[x+1][y]==0:
                cap.append((x,y))
            elif y+1<m and x+1<n and land[x+1][y]==0 and land[x][y+1]==0:
                cap.append((x,y))
            moves = [(1,0),(0,1),(-1,0),(0,-1)]
            for dx,dy in moves:
                nx = x+dx
                ny = y+dy
                if isvalid(nx,ny):
                    dfs(nx,ny)
        ans  = []
        for i in range(n):
            for j in range(m):
                if land[i][j]==1:
                    dfs(i,j)
                    ans.append([i,j,cap[-1][0],cap[-1][1]])
                    cap = []
        return ans
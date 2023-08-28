class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        def check(row,col):
            return 0<=row <len(grid) and 0<=col<len(grid) 
        queue = [(0,0)]
        c = 0
        while queue:
            row,col = queue.pop()
            if check(row,col):
                if check(row+2,col+1) and  grid[row+2][col+1] == grid[row][col]+1:
                    c+=1
                    queue.append([row+2,col+1])
                elif check(row+2,col-1) and grid[row+2][col-1] == grid[row][col]+1:
                    c+=1
                    queue.append([row+2,col-1])
                elif check(row+1,col+2) and grid[row+1][col+2] == grid[row][col]+1:
                    c+=1
                    queue.append([row+1,col+2])
                elif check(row+1,col-2) and grid[row+1][col-2] == grid[row][col]+1:
                    c+=1
                    queue.append([row+1,col-2])
                elif check(row-1,col+2) and grid[row-1][col+2] == grid[row][col]+1:
                    c+=1
                    queue.append([row-1,col+2])
                elif check(row-1,col-2) and grid[row-1][col-2] == grid[row][col]+1:
                    c+=1
                    queue.append([row-1,col-2])
                elif check(row-2,col+1) and grid[row-2][col+1] == grid[row][col]+1:
                    c+=1
                    queue.append([row-2,col+1])
                elif check(row-2,col-1) and grid[row-2][col-1] == grid[row][col]+1:
                    c+=1
                    queue.append([row-2,col-1])
                elif c==len(grid)*len(grid)-1:
                    return True
                print(c)
        return False

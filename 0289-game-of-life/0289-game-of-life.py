class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        
        def isvalid(i, j):
            return 0 <= i < row and 0 <= j < col
        
        def findOne(i, j):
            count_n = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if isvalid(ni, nj) and board[ni][nj] == 1:
                    count_n += 1
            
            return count_n
        
        ans = [[0 for _ in range(col)] for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                temp = findOne(i, j)
                if temp < 2 or temp > 3:
                    ans[i][j] = 0
                if temp==2 or temp==3:
                    ans[i][j] = board[i][j]
                if board[i][j]==0 and temp==3:
                    ans[i][j] = 1
        for i in range(row):
            for j in range(col):
                board[i][j] = ans[i][j]

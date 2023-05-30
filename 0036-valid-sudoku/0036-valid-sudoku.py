class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = []
        ans = True
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]!='.' and board[i][j] not in l:
                    l.append(board[i][j])
                    
                elif board[i][j]!='.' and board[i][j] in l:
                    ans = False
            l=[]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[j][i]!='.' and board[j][i] not in l:
                    l.append(board[j][i])
                elif board[j][i]!='.' and board[j][i] in l:
                    ans = False
            l=[]
        for m in range(0, 9, 3):
            for n in range(0, 9, 3):
                d = {}
                for i in range(n, n + 3):
                    for j in range(m, m + 3):
                        if board[i][j] == '.':
                            pass
                        elif board[i][j] in d:
                            return False
                        else:
                            d[board[i][j]] = True
        
        return ans
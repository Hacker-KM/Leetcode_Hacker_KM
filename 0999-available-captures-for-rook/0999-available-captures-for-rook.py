class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]=='R':
                    #3,4
                    x= i
                    y= j
                    print(x,y)
                    break
        ans = 0
        for i in range(y-1,-1,-1):
            if board[x][i]=='.':
                continue
            elif board[x][i]=='B':
                break
            else:
                print(board[x][i],1)
                ans+=1
                break
        for i in range(y+1,len(board)):
            if board[x][i]=='.':
                continue
            elif board[x][i]=='B':
                break
            else:
                print(board[x][i],2)

                ans+=1
                break
        l = []
        for i in range(len(board)):
            l.append(board[i][y])
        print(l)
        for i in range(x-1,-1,-1):
            if l[i]=='.':
                continue
            elif l[i]=='B':
                break
            else:
                print(l[i],3)

                ans+=1
                break
        for i in range(x+1,len(board)):
            if l[i]=='.':
                continue
            elif l[i]=='B':
                break
            else:
                print(l[i],4)
                ans+=1
                break 
        return ans


        




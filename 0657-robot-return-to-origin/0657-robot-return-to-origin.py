class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l = [0,0]
        for i in moves:
            if i=='U':
                l[1]+=1
            elif i=='D':
                l[1]-=1
            elif i=='L':
                l[0]-=1
            elif i=='R':
                l[0]+=1
        if l[0]==l[1]==0:
            return True
        return False

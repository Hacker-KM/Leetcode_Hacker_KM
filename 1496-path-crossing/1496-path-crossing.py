class Solution:
    def isPathCrossing(self, path: str) -> bool:
        points = [[0,0]]
        moves = {'N':[0,1],'E':[1,0],'S':[0,-1],'W':[-1,0]}
        start = [0,0]
        for i in path:
            curr = [start[0]+moves[i][0],start[1]+moves[i][1]]
            if curr in points:
                return True
            points.append(curr)
            start = curr
        return False
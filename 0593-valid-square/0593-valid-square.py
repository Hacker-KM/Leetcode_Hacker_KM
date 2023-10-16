class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(p,q):
            return (p[0]-q[0])**2 + (p[1]-q[1])**2

        l = [distance(p1,p2),distance(p1,p3),distance(p1,p4),distance(p4,p2),distance(p3,p4),distance(p3,p2)]
        l.sort()
        return l[0]==l[1]==l[2]==l[3] and l[4]==l[5] and l[0]>0
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for x,y in points:
            dic = {}
            for i,j in points:
                if x==i and y==j:
                    continue 
                distance = (x-i)*(x-i) + (y-j)*(y-j)
                if distance in dic:
                    ans+=2*dic[distance]
                    dic[distance] +=1
                else:
                    dic[distance] =1
        return ans
            

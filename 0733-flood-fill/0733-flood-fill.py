class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc] == color:
            return image

        r = len(image)        
        c = len(image[0]) 
        q= deque()    
        q.append((sr,sc))         
        
        visited = {(sr,sc)}    
        while q:              

            x,y = q.popleft()

            c1 = image[x][y]

            if x-1 >=0:
                if (x-1,y) not in visited and image[x-1][y] == c1 :
                    q.append((x-1,y))
                    visited.add((x-1,y))

                    
            if x+1 < r :
                if (x+1,y) not in visited and image[x+1][y] == c1:
                    q.append((x+1,y))
                    visited.add((x+1,y))

                   
            if y-1 >=0:
                if (x,y-1) not in visited and image[x][y-1] == c1:
                    q.append((x,y-1))
                    visited.add((x,y-1))


                    
            if y+1 < c :
                if (x,y+1) not in visited and image[x][y+1] == c1:
                    q.append((x,y+1))
                    visited.add((x,y+1))



        for i in visited:
            image[i[0]][i[1]] = color
                    
        return image
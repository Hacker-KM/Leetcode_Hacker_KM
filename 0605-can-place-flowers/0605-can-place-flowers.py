class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1:
            return flowerbed.count(0)>=n
        c=0
        if flowerbed[0]==0 and flowerbed[1] !=1:
            c+=1
            flowerbed[0]=1
        if flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2]!=1:
                c+=1
                flowerbed[len(flowerbed)-1]=1
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i]==0 and flowerbed[i-1]!=1 and flowerbed[i+1]!=1:
                print([flowerbed[i-1],flowerbed[i],flowerbed[i+1]])
                c+=1
                flowerbed[i] = 1
        return c>=n
        
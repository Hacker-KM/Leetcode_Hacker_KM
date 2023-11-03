class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target.sort()
        ans = []
        stack = []
        j = 0
        for i in range(1,n+1):
            if j==len(target):
                break
            ans.append('Push')
            if i!=target[j]:
                ans.append('Pop')
            else:
                j+=1
        return ans
            
                

        
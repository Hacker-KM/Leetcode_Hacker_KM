class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        i = 0
        ans = []
        while i+k<=n:
            taken = blocks[i:i+k]
            if taken.count('B')==k:
                return 0
            else:
                ans.append(taken.count('W'))
            i+=1
        return min(ans) if len(ans)>0 else 0
            
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        for i in nums:
            dic[i]+=1
        ans = 0
        for i in nums:
            if dic[k-i]>0 and dic[i]>0:
                if k-i==i and dic[i]>=2:
                    dic[i]-=2
                    ans+=1
                elif k-i!=i:
                    dic[k-i]-=1
                    dic[i] -=1
                    ans+=1
        return ans
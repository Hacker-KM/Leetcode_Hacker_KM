class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        pre_sum = [1 if nums[0]==1 else 0]
        for i in range(1,len(nums)):
            if nums[i]==1:
                if pre_sum[-1]>0:
                    pre_sum[-1]+=1
                else:
                    pre_sum.append(1)
            else:
                pre_sum.append(0)
        if len(pre_sum)==1:
            return pre_sum[0]-1 if pre_sum[-1]>0 else 0
        elif len(pre_sum)==2:
            return max(pre_sum)
        ans = 0
        for i in range(len(pre_sum)-2):
            ans = max(ans,pre_sum[i]+pre_sum[i+1]+pre_sum[i+2])
        return ans
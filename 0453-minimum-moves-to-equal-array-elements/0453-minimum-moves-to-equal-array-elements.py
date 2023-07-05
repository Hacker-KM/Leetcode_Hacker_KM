class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # mov = 0
        # nums.sort()
        # if len(set(nums))==2:
        #     return nums[-1]-nums[0]
        # if len(set(nums))==1:
        #         return mov
        # while mov<=max(nums)+1:
        #     if len(set(nums))==1:
        #         return mov
        #     nums.sort()
        #     for i in range(len(nums)-1):
        #         nums[i]+=1
        #     mov+=1
        # return -1

        # foolist question not by me
        mov = 0
        m = min(nums)
        for i in nums:
            d = i-m
            mov+=d
        return mov

            

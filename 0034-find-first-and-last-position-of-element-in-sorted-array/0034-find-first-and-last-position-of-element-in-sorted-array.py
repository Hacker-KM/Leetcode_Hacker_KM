class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = []
        for i in range(len(nums)):
            if nums[i]==target:
                l.append(i)
        print(l)
        if len(l)>2:
            return [l[0],l[-1]]
        elif len(l)==2:
            return l
        elif len(l)==1:
            return [l[0],l[0]]
        elif len(l)==0:
            return [-1,-1]
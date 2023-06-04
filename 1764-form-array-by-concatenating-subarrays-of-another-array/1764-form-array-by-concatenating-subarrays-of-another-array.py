class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        lg=len(groups)
        ind=0
        for i in groups:
            for j in range(ind,len(nums)):
                if nums[j:j+len(i)]==i:
                    ind=j+len(i)
                    lg-=1
                    break
        return lg==0
        

        
                    

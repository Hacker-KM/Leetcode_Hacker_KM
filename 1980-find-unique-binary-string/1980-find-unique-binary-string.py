class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        if not nums:
            return 0
        nums.sort(key=lambda x:int(x))
        check = 0
        for i in range(2**len(nums[0])):
            temp = bin(i).replace('0b','')
            temp = '0'*(len(nums[0])-len(temp))+temp
            if check<len(nums) and nums[check]!=temp:
                return temp
            elif check>len(nums)-1:
                return temp
            else:
                check+=1
        return ""
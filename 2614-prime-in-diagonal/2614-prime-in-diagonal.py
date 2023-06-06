class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        list1=[]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if i==j:
                    list1.append(nums[i][j])
                    list1.append(nums[i][len(nums)-1-i])
        answer=0
        for i in range(len(list1)):
                for j in range(2,int(sqrt(list1[i]))+1):
                    if list1[i]%j==0:
                        break
                else:
                    if list1[i]>answer:
                        answer=list1[i]
        if answer==1:
            return 0
        return answer
        
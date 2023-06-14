class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        if k==0:
            return nums
        while k>0:
            nums.insert(0,nums[-1])
            nums.pop()
            k-=1
        return nums
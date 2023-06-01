class Solution:
    def sortArray(self,nums):
        if len(nums) == 1:
            return nums
        middle_index = len(nums) // 2
        left_half = nums[:middle_index]
        right_half = nums[middle_index:]
        self.sortArray(left_half)
        self.sortArray(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j<len(right_half):
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i = i + 1
            else:
                nums[k] = right_half[j]
                j = j + 1
            k = k + 1
        while i < len(left_half):
            nums[k] = left_half[i]
            i = i + 1
            k = k + 1
        while j < len(right_half):
            nums[k] = right_half[j]
            j = j + 1
            k = k + 1
        return nums

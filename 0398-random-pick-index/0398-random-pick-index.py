class Solution:
    def __init__(self, nums):
        self.d = {}
        for i, v in enumerate(nums):
            if v in self.d:
                self.d[v].append(i)
            else:
                self.d[v] = [i]

    def pick(self, target):
        arr = self.d[target]
        return arr[random.randint(0, len(arr) - 1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
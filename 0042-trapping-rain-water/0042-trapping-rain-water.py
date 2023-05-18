class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0
        left_max = [0 for _ in range(len(height))]
        right_max = [0 for _ in range(len(height))]
        
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i - 1])
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i + 1])
        trapped = 0
        for i in range(1,len(height)-1):
            if min(left_max[i],right_max[i])>height[i]:
                trapped+=min(left_max[i],right_max[i])-height[i]
        return trapped


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        # if n-1>hour:
        #     return -1
        def calc_time(speed):
            time_taken = 0
            ## main logic is here the last time can be in decimal because there is no distance after it..........
            for i in dist[:-1]:
                time_taken+=ceil(i/speed)
            time_taken+=dist[-1]/speed
            return time_taken
        left = 1
        right = 10**7 +1

        while left<right:
            mid = (left+right)//2
            if calc_time(mid)<=hour:
                right = mid
            else:
                left = mid+1
        return left if left != 10**7 + 1 else -1

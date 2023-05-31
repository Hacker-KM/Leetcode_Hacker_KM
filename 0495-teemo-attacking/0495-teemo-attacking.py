class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        rep = 0
        for i in range(len(timeSeries)-1):
            diff = timeSeries[i+1] - timeSeries[i]
            if diff < duration:
                rep += duration - diff
        return len(timeSeries)*duration - rep
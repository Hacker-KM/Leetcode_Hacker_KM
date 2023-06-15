class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        tank = 0
        i = 0
        for j in range(len(gas)):
            tank +=gas[j]-cost[j]
            if tank<0:
                tank=0
                i = j+1
        return i
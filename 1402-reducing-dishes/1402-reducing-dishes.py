class Solution:
    def maxSatisfaction(self,satisfaction: List[int]) -> int:
        satisfaction.sort()

        total_satisfaction = 0
        max_total_satisfaction = 0
        num_dishes = len(satisfaction)

        for i in range(num_dishes - 1, -1, -1):
            if satisfaction[i] > -total_satisfaction:
                total_satisfaction += satisfaction[i]
                max_total_satisfaction += total_satisfaction
            else:
                break

        return max_total_satisfaction
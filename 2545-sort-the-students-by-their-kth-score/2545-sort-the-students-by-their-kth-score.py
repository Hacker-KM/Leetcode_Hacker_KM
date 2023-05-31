class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        sorted_list = sorted(score, key=lambda score:score[k])
        sorted_list.reverse()
        return sorted_list
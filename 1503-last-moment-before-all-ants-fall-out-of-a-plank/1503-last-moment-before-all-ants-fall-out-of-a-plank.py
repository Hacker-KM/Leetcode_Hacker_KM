class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if left ==[]:
            right.sort()
            return n-right[0]
        if right==[]:
            return max(left)
        right.sort()
        return max(max(left),n-right[0])
        
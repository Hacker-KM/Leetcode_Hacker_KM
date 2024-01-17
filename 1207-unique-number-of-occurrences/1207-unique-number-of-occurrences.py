class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        l = list(c.values())
        if len(set(l))!=len(l):
            return False
        return True
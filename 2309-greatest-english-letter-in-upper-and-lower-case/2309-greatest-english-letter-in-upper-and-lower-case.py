class Solution:
    def greatestLetter(self, s: str) -> str:
        a = [x for x in s if x.upper() in s and x.lower() in s] + [""]
        return max(a).upper()
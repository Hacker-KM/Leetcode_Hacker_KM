class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t= [""]*len(s)
        for i in indices:
            t[indices[i]] = s[i]
        return ''.join(i for i in t)
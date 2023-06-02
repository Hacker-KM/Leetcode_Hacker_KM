class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        l =[]
        for i in sentences:
            p = i.split()
            l.append(len(p))
        return max(l)
        
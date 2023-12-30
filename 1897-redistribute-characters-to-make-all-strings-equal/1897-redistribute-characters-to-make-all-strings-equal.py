class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        s = "".join(words)
        l = Counter(s)
        for i in l.values():
            if i%len(words)!=0:
                return False
        return True
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def check(word, start):
            for i in range(start, len(word)):
                if word[i].isupper():
                    return False
            return True
        
        l = []
        
        for word in queries:
            p1, p2 = 0, 0
            while p1 < len(word) and p2 < len(pattern):
                if word[p1] == pattern[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    if not word[p1].isupper() and pattern[p2].isupper():
                        p1 += 1
                    elif (word[p1].isupper() and pattern[p2].isupper()):
                        break
                    elif (not word[p1].isupper() and not pattern[p2].isupper()):
                        p1+=1
                    else:
                        break

            if p2 == len(pattern) and check(word, p1):
                l.append(True)
            else:
                l.append(False)
                
        return l
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited=set()
        ans = set()
        for i in range(len(s)-9):
            if s[i:i+10] in visited:
                ans.add(s[i:i+10])
            else:
                visited.add(s[i:i+10])
        return ans
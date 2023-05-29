class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l =0
        s = s.strip()
        for i in range(len(s)):
            if s[i] !=' ':
                l=l+1
                
            else:l =0
            
        return l
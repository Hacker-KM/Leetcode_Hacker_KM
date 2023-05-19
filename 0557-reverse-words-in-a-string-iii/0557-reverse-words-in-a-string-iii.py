class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(s.split(' '))
        s=''
        for i in l:
            i=i[::-1]
            s+=i+' '
        s = s[:len(s)-1]
        return s
            
        
            

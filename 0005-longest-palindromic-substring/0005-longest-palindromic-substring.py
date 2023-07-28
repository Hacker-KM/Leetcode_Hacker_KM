class Solution:
    def longestPalindrome(self, s: str) -> str:
        p=''
        i=0
        palin = []
        while i<len(s):
            for k in range(i,len(s)):
                p+=s[k]
                if p==p[::-1]:
                    palin.append(p)
                else:
                    continue
            p=''
            i+=1
        palin.sort(key=lambda x:len(x),reverse=True)
        return palin[0]

class Solution:
    def sortVowels(self, s: str) -> str:
        if not s:
            return None
        s= list(s)
        index=[]
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        v = []
        for i in range(len(s)):
            if s[i] in vowel:
                v.append(ord(s[i]))
                index.append(i)
        v.sort()
        for i in range(len(v)):
            v[i]= chr(v[i])
        k=0
        for i in index:
            s[i] = v[k]
            k+=1
        ans= ''.join(s)
        return ans
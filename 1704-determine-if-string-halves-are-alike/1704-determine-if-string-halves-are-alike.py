class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        va = vb = 0
        for i in range(len(a)):
            if a[i] in vowel:
                va+=1
            if b[i] in vowel:
                vb+=1
        return va==vb
            
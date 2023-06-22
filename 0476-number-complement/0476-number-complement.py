class Solution:
    def findComplement(self, num: int) -> int:
        s = bin(num).replace('0b','')
        s = list(s)
        for i in range(len(s)):
            if s[i]=='1':
                s[i]= '0'
            else:
                s[i]= '1'
        ans = ''
        ans = ans.join(s)
        return int(ans,2)
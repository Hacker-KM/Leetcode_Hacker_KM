class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = "aeiou"
        l= []
        for i in s:
            if i in vowel:
                l.append(1)
            else:
                l.append(0)
        p_sum = [l[0]]*len(l)
        for i in range(1,len(l)):
            p_sum[i] = p_sum[i-1]+l[i]
        ans = p_sum[k-1]
        for i in range(len(p_sum)-k):
            ans = max(ans,(p_sum[i+k]-p_sum[i]))
        return ans